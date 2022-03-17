import streamlit as st
import time
import pickle
import os
from Preparing_test_online import prepare_test_img, test

t0= time.time()
#print("Hello")

# Declaring variables
path = "db"
test_path = "test pictures"

def main():
    # Loading the model
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
    ["Demo app", "Attend from uploading image", "Attend using camera (photo mode)", "Training"])

    if app_mode == "Demo app":
        st.sidebar.write(" ------ ")
        photos = []
        images = os.listdir(test_path)

        for image in images:
            filepath = os.path.join(test_path, image)
            photos.append(image)
        
        option = st.sidebar.selectbox('Please select a sample image, then click Attend button', photos)
        pressed = st.sidebar.button('Attend')

        if pressed:
            st.sidebar.write('Please wait for the magic to happen!')
            pic = os.path.join(test_path, option)
            test_img, encoded_tests, face_test_locations = prepare_test_img(pic)

            ############----for trying only----------##########
            now = time.localtime()
            date = time.strftime("%Y/%m/%d", now)
            new_date = st.text_input('For Trying purposes you can put any date to test the program', date)
            ############----end trying----------##########

            df = test(encoded_tests, face_test_locations, test_img, encoded_trains, new_date)
            st.image(test_img)
            st.write(df)

    elif app_mode == "Attend from uploading image":     
        uploaded_file = st.file_uploader("Upload a picture of a person to make him attend", type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:   

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


    elif app_mode == "Attend using camera (photo mode)":
        picture = st.camera_input("Take a picture of yourself to attend")
        if picture is not None:

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
            import Training
            encoded_trains, images = Training.training(path)
            st.write(images)
            st.write(len(encoded_trains))
            output_file = 'encoded_faces.pickle'
            with open(output_file, 'wb') as f_out:
                pickle.dump(encoded_trains, f_out)


if __name__=='__main__':
    main()