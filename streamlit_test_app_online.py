import streamlit as st

import time
import cv2
import pickle
from Preparing_test_online import prepare_test_img, test

t0= time.time()
print("Hello")

# Declaring variables
path = "db"




def main():
    # Loading the mode
    @st.cache
    def load_model():
        with open ('encoded_faces.pickle', 'rb') as f_in:
            encoded_trains = pickle.load(f_in)
        return encoded_trains
    encoded_trains = load_model()

    # Start of the project
    st.title("Attendance_Project")
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Attend from image", "Attend using camera", "Training"])

    if app_mode == "Attend from image":     
        uploaded_file = st.file_uploader("Upload a picture of a person to make him attend", type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:   

            st.title("Here is the picture you've uploded")
            test_img, encoded_tests, face_test_locations = prepare_test_img(uploaded_file)
            
            ############----for trying only----------##########
            now = time.localtime()
            date = time.strftime("%Y/%m/%d", now)
            new_date = st.text_input('For Trying purposes you can put any date to test the program', date)
            ############----end trying----------##########

            df = test(encoded_tests, face_test_locations, test_img, encoded_trains, new_date)
            t1 = time.time() - t0
            st.write("Time elapsed: ", t1)

            st.image(test_img)
            st.write(df)





    elif app_mode == "Attend using camera":
        picture = st.camera_input("Take a picture of yourself to attend")
        if picture is not None:
            st.title("Here is the picture you've taken")

            test_img, encoded_tests, face_test_locations = prepare_test_img(picture)

            ############----for trying only----------##########
            now = time.localtime()
            date = time.strftime("%Y/%m/%d", now)
            new_date = st.text_input('For Trying purposes you can put any date to test the program', date)
            ############----end trying----------##########

            df = test(encoded_tests, face_test_locations, test_img, encoded_trains, new_date)

            t1 = time.time() - t0
            st.write("Time elapsed: ", t1)
            st.image(test_img)

            st.write(df)



    elif app_mode == "Training":
        st.subheader('Training Steps:')
        st.markdown("1. Get a photo of every employee with **only one face** in the picture.")
        st.markdown('2. Put all the photos in the **db** folder')
        st.markdown("3. Press **Train The Model** Button")
        if st.button("Train The Model"):
            from Training import training
            encoded_trains = training(path)



if __name__=='__main__':
    main()