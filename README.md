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

+ **Online Version:** <br>you can try it from [here](https://share.streamlit.io/abdassalamahmad/attendance_system/main/streamlit_test_app_online.py)
+ **Offline Version:** to try it follow these steps:
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
  * **Linux users**
```
sudo apt-get install cmake libgtk-3-dev freeglut3-dev
```
  * **Windows users**
- You need to install 
5. Run this command to try the offline version 












## To-Do List
- [x] Add penalty for comming late to work (After 9:00 AM)
- [ ] Detect 3D faces only (printed faces or rendered faces on screens shouldn't be detected)
