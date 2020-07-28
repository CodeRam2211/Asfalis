# Asfαlis(ασφαλής)
In light oof the recent pandemic ' covid 19' , this app was built for detecting people not wearing masks and can help you maintain distance fro these people.
This program consists of two parts 
Mask Detector Program built by Srijan using tensoflow lite , keras and android studio
### PC version
####  Initial Setup
This project requires python to be installed and python added to PATH variable in case of windows.
please run the following command in the MaskDetectorV2 directory using cmd 

        pip install -r requirements.txt
this directory consists of the files used to build the neural network consisted in the file train.py
##### Running the Project
go to the directory in which the project is present using cmd or terminal (as the case maybe) and run the following command:
         
         python capture.py

And if you want to retrain the model, download images into a folder "dataset" in the project directory and run 
        
        python train_mask.py
        
### ANDROID version
For this Download the project as a zip and run the apk file present in the Asfalis-APK on your android device. 
###### Note : Minimum android version required is ANDROID 8
On Opening the app you can either go into the detection screen by clicking on the power button or click on the help button for a quick walkthrough.

###### For viewing the source files you can open the Asfalis folder with ANDROID STUDIO ad let the gradle build itself

## Working of the Project

this project was made using tensorflow, a library to build Machine learning projects maintained by google. In this project tensorflow was used to build a neural network using about 1200 images collected in a dataset made by prajna Bhandhary you can obtain the images using this link https://github.com/prajnasb/observations.git or by the following command

         git clone https://github.com/prajnasb/observations.git
         
 after building the neural network it is saved as a tensorflow model and then converted to a tflite model. The mask classification works in two steps the program first detects or looks for the face and extracts the picture from it and runs an image classification on the face using the model created from before. It then classifies the facce by drawing a frame around the face with two colours along with the percentage of match
 ###### Green for with mask
 ###### Red for without mask
 
 ### Android Version
 the app was made using android studio and uses an algorithm to first detect a face and a frame is drawn around it and then extracted and classified using the dataset trained earlier.
 

