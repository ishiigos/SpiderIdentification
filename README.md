# SpiderIdentification
A key to identify spider species based on character selection by the user.

The following tutorial uses Git and Visual Studio Code. To install them use the following links:
Git - https://git-scm.com/downloads
VSCode - https://code.visualstudio.com/download

Run the Bayesian multi-entry interactive identification key using the following steps:

Step 1 :
Open git bash in the location you want to clone the code using the right click menu in the directory and clicking then clicking the 'Git Bash Here'

![unnamed](https://user-images.githubusercontent.com/75872231/234969176-47a62b53-f193-4d71-bac3-eac84a6a84e6.png)

Step 2: 
Clone the repository in Visual Studio Code using command 
git clone https://github.com/ishiigos/SpiderIdentification.git 
then press Enter

![unnamed](https://user-images.githubusercontent.com/75872231/234969606-82c53a16-6671-4003-af6a-2419715efe78.png)

Step 3: 
The code repository is cloned in your machine. 

![unnamed](https://user-images.githubusercontent.com/75872231/234969665-31f3f14b-1a19-4704-ab63-1cc6992716b5.png)

Step 4: 
Navigate to the SpiderIdentification folder that is newly created.

![unnamed](https://user-images.githubusercontent.com/75872231/234969735-bd564377-8739-4921-9c05-d85d77a739de.png)

Step 5:
Open this folder in visual studio code 

![unnamed](https://user-images.githubusercontent.com/75872231/234969812-73eb58d7-8b62-44dc-964e-4d069e8c3580.png)

Step 6: 
Download python in system using the link:
https://www.python.org/downloads/release/python-3113/

![unnamed](https://user-images.githubusercontent.com/75872231/234969879-20105c4d-f51a-41ff-8972-a83b5beb990b.png)

![unnamed](https://user-images.githubusercontent.com/75872231/234970013-2d48f680-c9fb-46c0-9b74-f212ec63eba3.png)

Note: Python pass should be added to the environment variables of the system. If not added in the first time install you can modify the installation and check this option to add it 

![unnamed](https://user-images.githubusercontent.com/75872231/234970091-42cfb835-3ef3-40f4-be78-23dd0ce30612.png)

Step 7: 
Reopen Visual Studio Code, and Install extension for Python in Visual Studio using the extensions

![unnamed](https://user-images.githubusercontent.com/75872231/234970164-89208d95-da26-4812-a0c2-c3291a90984e.png)

Step 8: 
Install the required packages for the code to work using the terminal window (Open terminal window using the keyboard keys (Ctrl + ~)
pip install flask
pip install CORS 
pip install -U flask-cors

![unnamed](https://user-images.githubusercontent.com/75872231/234970210-cbe45f81-44ab-4db3-a1c4-9dc851f90849.png)

![unnamed](https://user-images.githubusercontent.com/75872231/234970244-cfe52a60-bd77-4e7f-8161-36d5a4199f35.png)

Step 9: 
Run the api using the command below in the terminal
python -m flask run

![unnamed](https://user-images.githubusercontent.com/75872231/234970321-15ec0a3c-79b9-4450-a889-f03e60fb63b2.png)

Step 10: 
Open the html file in the browser to run the UI.

![unnamed](https://user-images.githubusercontent.com/75872231/234970361-5362d218-2b9e-4761-9da9-61080faae2e0.png)

Note: Once the key has been initialized, it can be used indefinitely. It may stop working in case the API has been stopped using Ctrl + C in the terminal window, or the run time has been stopped.
