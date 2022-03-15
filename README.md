[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/abdassalamahmad/attendance_system/main/streamlit_test_app_online.py)
# Attendance-System-Real-Time
Attendance System using Face Recognition (HOG) Real-Time

## Model Demo

https://user-images.githubusercontent.com/83673888/158333701-9f2cffd8-cd91-496b-98f7-94702bf4bcb6.mp4

## How To Try This Model
There are two versions (Online and Offline) 

|                                 | Online                                         | Offline     |
| --------------------------------| :--------------------------------------------: | :------------------------------------------------------------: |
| Training                        | - Only the host (me) can train new faces.      | - When you clone the repo you can train new faces as you want. |
| Attend from Uploading Photo     | <li>- [x] </li>                                | <li>- [x] </li>                                                |
| Attend from Camera (Photo Mode) | <li>- [x] </li>                                | <li>- [x] </li>                                                |
| Attend Live                     | <li>- [ ] </li>                                | <li>- [x] </li>                                                |

#### **Online Version:** <br>you can try it from [here](https://share.streamlit.io/abdassalamahmad/attendance_system/main/streamlit_test_app_online.py)
#### **Offline Version:** <br>Follow these steps to try it:
1. Clone this repo to get all the code and pre-trained model(pickle_file).
2. Change current directory into the cloned repo folder.
3. Install all of the libraries from [environment.yml](https://github.com/AbdassalamAhmad/Attendance_System/blob/main/environment.yml) file by using these commands.
```
conda env create -f environment.yml
conda activate attendance
```
(optional step) to check if all libraries installed
```
conda env list
```
4. Install all of the dependencies from [packages.txt](https://github.com/AbdassalamAhmad/Attendance_System/blob/main/packages.txt) using this command.
  - **Linux users**: cmake is a must.
```
sudo apt-get install cmake libgtk-3-dev freeglut3-dev
```
  - **Windows users**:<br> You need to install visual studio community version from [here](https://visualstudio.microsoft.com/downloads/) and make sure that cmake is checked when installing because it is a must.
5. Run this script [streamlit_local_app_bussines_ready.py](https://github.com/AbdassalamAhmad/Attendance_System/blob/main/streamlit_local_app_bussines_ready.py) to try the offline version by running this code in the cloned repo directory after installing all dependencies.
```py
streamlit run streamlit_local_app_bussines_ready.py
```

### Training:
To train the model on different faces, do the following:
1. Get a photo that contains one person and rename it to the person's name and put it in the `db` folder like this picture.<br>
![image](https://user-images.githubusercontent.com/83673888/158378862-30e4cce9-a737-4079-ae8c-99a013ea7460.png)<br>
2. Repeat that for as many faces as you want.
3. Finally run the [streamlit_local_app_bussines_ready.py](https://github.com/AbdassalamAhmad/Attendance_System/blob/main/streamlit_local_app_bussines_ready.py) script, and put it on Training mode and press the `Train The Model` button then you can go for testing.

### Testing:
You have three modes. The best one is **Live Attendance** (Real case scenario)<br>
To run it do the following:
1. From the sidebar select `Attend Live` mode.
2. Select `Attendance.csv` file, which is a file to record the arrival_time, date, penalty of every attendant.
3. Check `run` box to start the program the show faces of people you trained (people in `db` folder)









## To-Do List
- [x] Penalty (10$) for comming late to work (After 9:00 AM)
- [ ] Detect 3D faces only (printed faces or rendered faces on screens shouldn't be detected)
