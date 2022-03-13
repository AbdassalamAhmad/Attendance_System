import time
import cv2
import pickle
from Preparing import prepare_test_img, test

t0= time.time()
print("Hello")


# Declaring variables
path = "db"
test_img = 'db\Bill Gates.jpg'

########-------- for importing training--------##########
# val = input("Enter your value: ")
# if val =='1':
#     from Training import training
#     encoded_trains = training(path)

# Reading database faces
# 
with open ('encoded_faces.pickle', 'rb') as f_in:
    encoded_trains = pickle.load(f_in)

# Preparing testing
test_img, encoded_tests, face_test_locations = prepare_test_img(test_img)

# Testing
attendance_list, df = test(encoded_tests, face_test_locations, test_img, encoded_trains)
t1 = time.time() - t0
print("Time elapsed: ", t1)
test_img = cv2.resize(test_img,(0,0),None,0.50,0.50) 
cv2.imshow('Test',test_img)
cv2.waitKey(0)
print (df)
#print(attendance_list)
