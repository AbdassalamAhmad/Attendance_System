import streamlit as st
import time
import cv2
import pickle
import face_recognition
from Preparing_local import prepare_test_img, test

t0= time.time()
# print("Hello")
# Declaring variables
path = "db"


def main():
    # Loading the mode
    #@st.cache
    def load_model():
        with open ('encoded_faces.pickle', 'rb') as f_in:
            encoded_trains = pickle.load(f_in)
        return encoded_trains
    encoded_trains = load_model()

    # Start of the project
    st.title("Attendance_Project")
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
    ["Attend from image", "Attend using camera", "Training", "Attend Live"])


    if app_mode == "Attend from image":     
        attendance_file = st.file_uploader("Choose attendance file",type =['csv'])
        uploaded_file = st.file_uploader("Upload a picture of a person to make him attend", type=['jpg', 'jpeg', 'png'])
        if attendance_file is not None and uploaded_file is not None:   

            test_img, encoded_tests, face_test_locations = prepare_test_img(uploaded_file)
            df = test(encoded_tests, face_test_locations, test_img, encoded_trains, attendance_file)
            t1 = time.time() - t0

            st.write("Time elapsed: ", t1)
            # test_img = cv2.resize(test_img,(0,0),None,0.50,0.50) 
            st.image(test_img)
            st.write(df)


    elif app_mode == "Attend using camera":
        attendance_file = st.file_uploader("Choose attendance file",type =['csv'])
        picture = st.camera_input("Take a picture")
        if picture is not None and attendance_file is not None:

            test_img, encoded_tests, face_test_locations = prepare_test_img(picture)
            df = test(encoded_tests, face_test_locations, test_img, encoded_trains, attendance_file)
            t1 = time.time() - t0

            st.write("Time elapsed: ", t1)
            #test_img = cv2.resize(test_img,(0,0),None,0.50,0.50) 
            st.image(test_img)
            st.write(df)


    elif app_mode == "Training":
        st.subheader('Training Steps:')
        st.markdown("1. Get a photo of every employee with **only one face** in the picture.")
        st.markdown('2. Put all the photos in the **db** folder')
        st.markdown("3. Press **Train The Model** Button")

        if st.button("Train The Model"):
            import Training
            encoded_trains, images = Training.training(path)
            st.write(images)
            st.write(len(encoded_trains))
            output_file = 'encoded_faces.pickle'

            with open(output_file, 'wb') as f_out:
                pickle.dump(encoded_trains, f_out)
            

    elif app_mode == "Attend Live":
        st.title("Webcam Live Feed")
        attendance_file = st.file_uploader("Choose attendance file",type =['csv'])

        if attendance_file is not None:
            run = st.checkbox('Run')
            FRAME_WINDOW = st.image([])
            camera = cv2.VideoCapture(0)

            while run:
                _, test_img = camera.read()
                test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
                test_img_small = cv2.resize(test_img,(0,0),None,0.5,0.5)

                face_test_locations = face_recognition.face_locations(test_img_small, model = "hog")
                encoded_tests = face_recognition.face_encodings(test_img_small)
                df = test(encoded_tests, face_test_locations, test_img, encoded_trains, attendance_file)
                #st.image(test_img)
                FRAME_WINDOW.image(test_img)
                #st.write(df)
            else:
                st.write('Stopped')


if __name__=='__main__':
    main()