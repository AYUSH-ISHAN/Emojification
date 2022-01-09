
# FACIAL EXPRESSION TO EMOJIS:- 

<h2>INTRODUCTION:<h2>
 This project is based on Computer Vision which detects your facial expression and converts it to an emoji!<br>
 
<h2>DATASET:</h2>
 The data consists of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centered and occupies about the same amount of space in each image. The task is to categorize each face based on the emotion shown in the facial expression in to one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral).

train.csv contains two columns, "emotion" and "pixels". The "emotion" column contains a numeric code ranging from 0 to 6, inclusive, for the emotion that is present in the image. The "pixels" column contains a string surrounded in quotes for each image. The contents of this string a space-separated pixel values in row major order. test.csv contains only the "pixels" column and your task is to predict the emotion column.

The training set consists of 28,709 examples. The public test set used for the leaderboard consists of 3,589 examples. The final test set, which was used to determine the winner of the competition, consists of another 3,589 examples.


 * [Dataset](https://drive.google.com/drive/folders/1H8mDV5qPHQOWSlVAil6mivBkHJx9YcDi?usp=sharing) used is from a [kaggle contest](
https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data).

 
 
 ## Model Training approaches we used
<h3><B>CNN on Kaggle dataset</B></h3>
 
 <h4>Model Structure: </h4>
 
              Model: "sequential"
              _________________________________________________________________
              Layer (type)                 Output Shape              Param #   
              =================================================================
              conv2d (Conv2D)              (None, 48, 48, 64)        640       
              _________________________________________________________________
              batch_normalization (BatchNo (None, 48, 48, 64)        256       
              _________________________________________________________________
              activation (Activation)      (None, 48, 48, 64)        0         
              _________________________________________________________________
              dropout (Dropout)            (None, 48, 48, 64)        0         
              _________________________________________________________________
              conv2d_1 (Conv2D)            (None, 48, 48, 128)       73856     
              _________________________________________________________________
              batch_normalization_1 (Batch (None, 48, 48, 128)       512       
              _________________________________________________________________
              activation_1 (Activation)    (None, 48, 48, 128)       0         
              _________________________________________________________________
              max_pooling2d (MaxPooling2D) (None, 24, 24, 128)       0         
              _________________________________________________________________
              dropout_1 (Dropout)          (None, 24, 24, 128)       0         
              _________________________________________________________________
              conv2d_2 (Conv2D)            (None, 24, 24, 512)       590336    
              _________________________________________________________________
              batch_normalization_2 (Batch (None, 24, 24, 512)       2048      
              _________________________________________________________________
              activation_2 (Activation)    (None, 24, 24, 512)       0         
              _________________________________________________________________
              max_pooling2d_1 (MaxPooling2 (None, 12, 12, 512)       0         
              _________________________________________________________________
              dropout_2 (Dropout)          (None, 12, 12, 512)       0         
              _________________________________________________________________
              conv2d_3 (Conv2D)            (None, 12, 12, 512)       2359808   
              _________________________________________________________________
              batch_normalization_3 (Batch (None, 12, 12, 512)       2048      
              _________________________________________________________________
              activation_3 (Activation)    (None, 12, 12, 512)       0         
              _________________________________________________________________
              max_pooling2d_2 (MaxPooling2 (None, 6, 6, 512)         0         
              _________________________________________________________________
              dropout_3 (Dropout)          (None, 6, 6, 512)         0         
              _________________________________________________________________
              flatten (Flatten)            (None, 18432)             0         
              _________________________________________________________________
              dense (Dense)                (None, 256)               4718848   
              _________________________________________________________________
              batch_normalization_4 (Batch (None, 256)               1024      
              _________________________________________________________________
              activation_4 (Activation)    (None, 256)               0         
              _________________________________________________________________
              dropout_4 (Dropout)          (None, 256)               0         
              _________________________________________________________________
              dense_1 (Dense)              (None, 512)               131584    
              _________________________________________________________________
              batch_normalization_5 (Batch (None, 512)               2048      
              _________________________________________________________________
              activation_5 (Activation)    (None, 512)               0         
              _________________________________________________________________
              dropout_5 (Dropout)          (None, 512)               0         
              _________________________________________________________________
              dense_2 (Dense)              (None, 7)                 3591      
              =================================================================
              Total params: 7,886,599
              Trainable params: 7,882,631
              Non-trainable params: 3,968
              _________________________________________________________________


 
<h3><B>BaseModel_Resnet - Resnet on Kaggle Dataset</B></h3>
 
 <h4>Model Structure: </h4>
 
                _________________________________________________________________
               Layer (type)                 Output Shape              Param #   
               =================================================================
               lambda_1 (Lambda)            (None, 48, 48, 3)         0         
               _________________________________________________________________
               resnet50 (Functional)        (None, 2, 2, 2048)        23587712  
               _________________________________________________________________
               flatten_1 (Flatten)          (None, 8192)              0         
               _________________________________________________________________
               batch_normalization_4 (Batch (None, 8192)              32768     
               _________________________________________________________________
               dense_4 (Dense)              (None, 256)               2097408   
               _________________________________________________________________
               dropout_3 (Dropout)          (None, 256)               0         
               _________________________________________________________________
               batch_normalization_5 (Batch (None, 256)               1024      
               _________________________________________________________________
               dense_5 (Dense)              (None, 128)               32896     
               _________________________________________________________________
               dropout_4 (Dropout)          (None, 128)               0         
               _________________________________________________________________
               batch_normalization_6 (Batch (None, 128)               512       
               _________________________________________________________________
               dense_6 (Dense)              (None, 64)                8256      
               _________________________________________________________________
               dropout_5 (Dropout)          (None, 64)                0         
               _________________________________________________________________
               batch_normalization_7 (Batch (None, 64)                256       
               _________________________________________________________________
               dense_7 (Dense)              (None, 7)                 455       
               =================================================================
               Total params: 25,761,287
               Trainable params: 17,132,295
               Non-trainable params: 8,628,992
               _________________________________________________________________
 
 Now, here 'lambda' denotes the Resnets architecture as the base model.
  
<h3><B>Neural network on facial landmarks from dlib on kaggle dataset</B></h3>
  
 <h4> Preprocessing:-</h4>
 
Obtained the facial landmaarks using the [dlib-opencv library](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/) on the images. Facial landmarks are used to localize and represent salient regions of the face, such as:


 * Eyes<br>
 * Eyebrows<br>
 * Nose<br>
 * Mouth<br>
 * Jawline<br>

 These points are quite sensitive to emotions. So, we trained our model on the relative positions of the jaw, eyes and other salient features.<br><br>
 <B>BELOW SHOWN IMAGES ARE SOME DEMO OF DILIB :</B><br>
 
 <img src = "https://github.com/AYUSH-ISHAN/Emoji_Prediction_Project/blob/main/facial_landmarks_example_01_result.jpg" height = "390" width = "390" align = "left"/>
 <img src = "https://github.com/AYUSH-ISHAN/Emoji_Prediction_Project/blob/main/Visualizing-the-68-facial-landmark-coordinates-from-Dlib-landmark-detector-1_Q640.jpg" height = "390" wodth = "390" align = "right"/><br>
 <br>
<h4>Model Architeture : <h4>
 
             Model: "sequential"
            _________________________________________________________________
            Layer (type)                 Output Shape              Param #   
            =================================================================
            conv2d (Conv2D)              (None, 68, 2, 128)        256       
            _________________________________________________________________
            batch_normalization (BatchNo (None, 68, 2, 128)        512       
            _________________________________________________________________
            max_pooling2d (MaxPooling2D) (None, 34, 1, 128)        0         
            _________________________________________________________________
            conv2d_1 (Conv2D)            (None, 34, 1, 128)        16512     
            _________________________________________________________________
            batch_normalization_1 (Batch (None, 34, 1, 128)        512       
            _________________________________________________________________
            conv2d_2 (Conv2D)            (None, 34, 1, 256)        33024     
            _________________________________________________________________
            batch_normalization_2 (Batch (None, 34, 1, 256)        1024      
            _________________________________________________________________
            max_pooling2d_1 (MaxPooling2 (None, 17, 1, 256)        0         
            _________________________________________________________________
            conv2d_3 (Conv2D)            (None, 17, 1, 256)        65792     
            _________________________________________________________________
            batch_normalization_3 (Batch (None, 17, 1, 256)        1024      
            _________________________________________________________________
            conv2d_4 (Conv2D)            (None, 17, 1, 256)        65792     
            _________________________________________________________________
            batch_normalization_4 (Batch (None, 17, 1, 256)        1024      
            _________________________________________________________________
            max_pooling2d_2 (MaxPooling2 (None, 9, 1, 256)         0         
            _________________________________________________________________
            conv2d_5 (Conv2D)            (None, 9, 1, 256)         65792     
            _________________________________________________________________
            batch_normalization_5 (Batch (None, 9, 1, 256)         1024      
            _________________________________________________________________
            conv2d_6 (Conv2D)            (None, 9, 1, 128)         32896     
            _________________________________________________________________
            batch_normalization_6 (Batch (None, 9, 1, 128)         512       
            _________________________________________________________________
            max_pooling2d_3 (MaxPooling2 (None, 5, 1, 128)         0         
            _________________________________________________________________
            conv2d_7 (Conv2D)            (None, 5, 1, 64)          8256      
            _________________________________________________________________
            batch_normalization_7 (Batch (None, 5, 1, 64)          256       
            _________________________________________________________________
            flatten (Flatten)            (None, 320)               0         
            _________________________________________________________________
            dense (Dense)                (None, 7)                 2247      
            =================================================================
            Total params: 296,455
            Trainable params: 293,511
            Non-trainable params: 2,944
            _________________________________________________________________

<h3><B>Support Vector Machine on facial landmarks from dlib on kaggle dataset</B></h3>
 
 <img src = "https://github.com/AYUSH-ISHAN/Emoji_Prediction_Project/blob/main/svm.jpeg" height= "300" width = "300" align="center"/><br>
 
<h3><B>CNN on AffectNet Dataset</B></h3>
  
 <h4>Model Architecure: </h4>
 
           Model: "sequential_1"
           _________________________________________________________________
           Layer (type)                 Output Shape              Param #   
           =================================================================
           conv2d_4 (Conv2D)            (None, 224, 224, 64)      1792      
           _________________________________________________________________
           batch_normalization_6 (Batch (None, 224, 224, 64)      256       
           _________________________________________________________________
           activation_6 (Activation)    (None, 224, 224, 64)      0         
           _________________________________________________________________
           dropout_6 (Dropout)          (None, 224, 224, 64)      0         
           _________________________________________________________________
           conv2d_5 (Conv2D)            (None, 224, 224, 128)     73856     
           _________________________________________________________________
           batch_normalization_7 (Batch (None, 224, 224, 128)     512       
           _________________________________________________________________
           activation_7 (Activation)    (None, 224, 224, 128)     0         
           _________________________________________________________________
           max_pooling2d_3 (MaxPooling2 (None, 112, 112, 128)     0         
           _________________________________________________________________
           dropout_7 (Dropout)          (None, 112, 112, 128)     0         
           _________________________________________________________________
           conv2d_6 (Conv2D)            (None, 112, 112, 512)     590336    
           _________________________________________________________________
           batch_normalization_8 (Batch (None, 112, 112, 512)     2048      
           _________________________________________________________________
           activation_8 (Activation)    (None, 112, 112, 512)     0         
           _________________________________________________________________
           max_pooling2d_4 (MaxPooling2 (None, 56, 56, 512)       0         
           _________________________________________________________________
           dropout_8 (Dropout)          (None, 56, 56, 512)       0         
           _________________________________________________________________
           conv2d_7 (Conv2D)            (None, 56, 56, 512)       2359808   
           _________________________________________________________________
           batch_normalization_9 (Batch (None, 56, 56, 512)       2048      
           _________________________________________________________________
           activation_9 (Activation)    (None, 56, 56, 512)       0         
           _________________________________________________________________
           max_pooling2d_5 (MaxPooling2 (None, 28, 28, 512)       0         
           _________________________________________________________________
           dropout_9 (Dropout)          (None, 28, 28, 512)       0         
           _________________________________________________________________
           flatten_1 (Flatten)          (None, 401408)            0         
           _________________________________________________________________
           dense_3 (Dense)              (None, 256)               102760704 
           _________________________________________________________________
           batch_normalization_10 (Batc (None, 256)               1024      
           _________________________________________________________________
           activation_10 (Activation)   (None, 256)               0         
           _________________________________________________________________
           dropout_10 (Dropout)         (None, 256)               0         
           _________________________________________________________________
           dense_4 (Dense)              (None, 128)               32896     
           _________________________________________________________________
           batch_normalization_11 (Batc (None, 128)               512       
           _________________________________________________________________
           activation_11 (Activation)   (None, 128)               0         
           _________________________________________________________________
           dropout_11 (Dropout)         (None, 128)               0         
           _________________________________________________________________
           dense_5 (Dense)              (None, 6)                 774       
           =================================================================
           Total params: 105,826,566
           Trainable params: 105,823,366
           Non-trainable params: 3,200
           _________________________________________________________________


 # Results: 
 
 
 
