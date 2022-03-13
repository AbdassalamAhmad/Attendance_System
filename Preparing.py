import cv2
from cv2 import dft
#import numpy as np
import face_recognition
import os
import time
import pandas as pd

# Declaring variables
path = "db"
scale = 2

def late_penalty(arrive_time):
    penalty = 0
    if int(arrive_time[0:2])> 8:
        penalty = 10
    return penalty

def markattendance(person_name, attendance_file):

    with open(attendance_file.name,'r+') as f:
        lines = f.readlines()
        name_list=[]
        now = time.localtime()
        date = time.strftime("%Y/%m/%d", now)
        for line in lines:
            entry = line.split(',')
            if entry[2] == date:
                name_list.append(entry[0])
        if person_name not in name_list:
            arrive_time = time.strftime("%H:%M:%S", now)
            penalty = late_penalty(arrive_time)
            f.writelines(f'\n{person_name},{arrive_time},{date},{penalty}')


            
    f = open(attendance_file.name,'r',encoding = 'utf-8')
    df = pd.read_csv(f)
    return df





def prepare_test_img(test_img):
    test_img = face_recognition.load_image_file(test_img)
    #test_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2RGB)
    test_img_small = cv2.resize(test_img,(0,0),None,0.5,0.5)

    face_test_locations = face_recognition.face_locations(test_img_small, model = "hog")
    encoded_tests = face_recognition.face_encodings(test_img_small)
    return test_img, encoded_tests, face_test_locations


def test(encoded_tests, face_test_locations, test_img, encoded_trains, attendance_file):
    images = os.listdir(path)
    name_indices = []
    names=[]

    for encoded_test, face_test_location in zip(encoded_tests, face_test_locations):
        results = face_recognition.compare_faces(encoded_trains,encoded_test,tolerance=0.5)

        if True in results:
            name_index = results.index(True)
            name_indices.append(name_index)
            for count, image in enumerate(images):
                if count == name_index:
                    person_name = image.split(".")[0]
                    top_left, bottom_right = (face_test_location[3]*scale, face_test_location[0]*scale) ,(face_test_location[1]*scale, face_test_location[2]*scale)
                    cv2.rectangle(test_img,(top_left),(bottom_right),(255,0,255),2)
                    cv2.rectangle(test_img,(bottom_right),(top_left[0], bottom_right[1]+30),(255,0,255),cv2.FILLED)
                    cv2.putText(test_img,person_name,(top_left[0]+6,bottom_right[1]+25),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                    df=markattendance(person_name, attendance_file)
        else:
            top_left, bottom_right = (face_test_location[3]*scale, face_test_location[0]*scale) ,(face_test_location[1]*scale, face_test_location[2]*scale)
            cv2.rectangle(test_img,(top_left),(bottom_right),(255,0,255),2)
            cv2.rectangle(test_img,(bottom_right),(top_left[0], bottom_right[1]+30),(255,0,255),cv2.FILLED)
            cv2.putText(test_img,"UNKNOWN",(top_left[0]+6,bottom_right[1]+25),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
            f = open(attendance_file.name,'r',encoding = 'utf-8')
            df = pd.read_csv(f)

    attendance_list = [False for i in range(len(results))]
    for i in name_indices:
        attendance_list[i] = True

    for image in images:
        names.append(image.split(".")[0])

    ans = {}
    for i, name in enumerate (names):
        ans[name] = attendance_list[i]


    return (ans,df)






