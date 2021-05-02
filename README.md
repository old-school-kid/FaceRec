# FaceRec
An innovative way to mark attenence using face recognition.

# Dependencies

To run the project locally make sure to have the following dependencies installed on your system.

1. flask
2. flask-lgoin
3. flask SQL Alchemy
4. OpenCV
5. xlrd

# Our solution
The images are captured and saved during the registration of each student in a database.
A model is trained to differentiate between real live fed video and photographs 
The model first predicts if it is a real human. If it is a real human face then the siamese network comes into action.
The siamese network compares photo with all the photo using cosine similarity. If the similarity is above a certain threshold then the person is marked present and the date and time is also noted
This data in turn will be saved as a csv file for future reference.


# Machine Learning
1. The face-recognition package which has more than 99% accuracy detects face and encodes them
2. This encoding is fed into a siamese network to compare the cosine similarity 
3. A threshold (95%) is set. Faces above this similarity are recognized
4. A model is trained to classify real live image from photos which checks the liveliness

