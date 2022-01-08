
# FACIAL EXPRESSION TO EMOJIS:- 

<h2>INTRODUCTION:<h2>
 This project is based on Computer Vision which detects your facial expression and converts it to an emoji!<br>
 
<h2>DATASET:</h2>
 The data consists of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centered and occupies about the same amount of space in each image. The task is to categorize each face based on the emotion shown in the facial expression in to one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral).

train.csv contains two columns, "emotion" and "pixels". The "emotion" column contains a numeric code ranging from 0 to 6, inclusive, for the emotion that is present in the image. The "pixels" column contains a string surrounded in quotes for each image. The contents of this string a space-separated pixel values in row major order. test.csv contains only the "pixels" column and your task is to predict the emotion column.

The training set consists of 28,709 examples. The public test set used for the leaderboard consists of 3,589 examples. The final test set, which was used to determine the winner of the competition, consists of another 3,589 examples.


 * [Dataset](https://drive.google.com/drive/folders/1H8mDV5qPHQOWSlVAil6mivBkHJx9YcDi?usp=sharing) used is from a [kaggle contest](
https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data).

 
 <h2> Preprocessing:-</h2>
 
Obtained the facial landmaarks using the [dlib-opencv library](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/) on the images. Facial landmarks are used to localize and represent salient regions of the face, such as:

 
 * Eyes<br>
 * Eyebrows<br>
 * Nose<br>
 * Mouth<br>
 * Jawline<br>
 
 These points are quite sensitive to emotions. So, we trained our model on the relative positions of the jaw, eyes and other salient features.<br><br>
 BELOW SHOWN IMAGES ARE SOME DEMO OF DILIB :<br>
 <p align = "center">
 <img src = "https://github.com/AYUSH-ISHAN/Emoji_Prediction_Project/blob/main/facial_landmarks_example_01_result.jpg" height = "512" width = "512" align = "center"><br>
 <br>
 <img src = "https://github.com/AYUSH-ISHAN/Emoji_Prediction_Project/blob/main/Visualizing-the-68-facial-landmark-coordinates-from-Dlib-landmark-detector-1_Q640.jpg" height = "512" wodth = "512"><br>
 </p>

 <h2> Training the model:- </h2>
 
 
 
