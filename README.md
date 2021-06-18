# FaceRec
An innovative way to mark attenence using face recognition.

## Table of Contents

- [Problem Statement](#Problem-Statement)
- [Solution](#Our-solution)
- [Machine Learning](#Machine-Learning)
- [Dependecies](#Dependencies)
- [How to run](#Instruction)
- [Demo](#Demo)
- [Project Links](#Important-links)


## Problem Statement
Online education, though the need of the hour, has also given rise to a lot of instances of students missing classes and cheating. So, we need a robust and innovative system for attendance marking, which is altered for this particular situation.

## Our solution
The images are captured and saved during the registration of each student in a database.
A model is trained to differentiate between real live fed video and photographs 
The model first predicts if it is a real human. If it is a real human face then the siamese network comes into action.
The siamese network compares photo with all the photo using cosine similarity. If the similarity is above a certain threshold then the person is marked present and the date and time is also noted
This data in turn will be saved as a csv file for future reference.


## Machine Learning
1. The face-recognition package which has more than 99% accuracy detects face and encodes them
2. This encoding is fed into a siamese network to compare the cosine similarity 
3. A threshold (95%) is set. Faces above this similarity are recognized
4. A model is trained to classify real live image from photos which checks the liveliness

## Dependencies

To run the project locally make sure to have the following dependencies installed on your system.

1. flask
2. flask-lgoin
3. flask SQL Alchemy
4. OpenCV
5. pandas
6. Keras
7. Tensorflow
8. face-recognition
9. pyhton-3.x

## Instruction
1. Clone the project
2. Install all the dependencies
 ```
pip install requirements.txt
```
3. Save photos in People folder
4. execute while in the directory
 ```
python app.py
```

## Demo
The model recognizes the person and marks his/her attendance while recognizing possible fakes like images.
![Demo](https://github.com/old-school-kid/FaceRec/blob/main/images/FaceRec.gif?raw=true)

## Important Links
[Presentation](https://docs.google.com/presentation/d/16Qo8kPsEAf80XfjHPQvojUBLmF5acv4QFXHnp_-rSnk/edit?usp=sharing)
