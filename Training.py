import cv2
import face_recognition
import os
# import streamlit as st
# import pickle
# Declaring variables
path = "db"

def training(path):
    images = os.listdir(path)  
    encoded_trains =[]

    for image in images:
        train_img = face_recognition.load_image_file(f"db/{image}")
        train_img = cv2.cvtColor(train_img,cv2.COLOR_BGR2RGB)
        encoded_trains.append(face_recognition.face_encodings(train_img)[0])
    return encoded_trains, images


# encoded_trains, images = training(path)
# st.write(images)
# output_file = 'encoded_faces.pickle'
# with open(output_file, 'wb') as f_out:
#     pickle.dump(encoded_trains, f_out)
