# Dog vs Cat

### <i> Try it yourself - https://kanakmi-dogvscat.herokuapp.com/ </i>
<br>

[![Cover Image](https://github.com/kanakmi/dogvscat/blob/main/Cover.png?raw=True)](https://kanakmi-dogvscat.herokuapp.com/)

## Tech Stack

![Python](https://img.shields.io/badge/Python-v3.8-red?style=flat-square&logo=python&logoColor=red)
![Tensorflow](https://img.shields.io/badge/tensorflow-v2.3.0-orange?style=flat-square&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-v2.0.1-brightgreen?style=flat-square&logo=flask&logoColor=brightgreen)
![HTML](https://img.shields.io/badge/HTML-5-blueviolet?style=flat-square&logo=html5&logoColor=blueviolet)
![CSS](https://img.shields.io/badge/CSS-3-blue?style=flat-square&logo=css3&logoColor=blue)
![JS](https://img.shields.io/badge/JAVASCRIPT--black?style=flat-square&logo=javascript)

## Overview

The classic AI problem to classify images of Cats and Dogs.<br>
The CNN model uses 8000 images (4000 each of Cat and Dog) for the classification task.<br>
The Dataset is taken from Kaggle and the link for the same is https://www.kaggle.com/chetankv/dogs-cats-images <br>
After Image Augmentation, the total number of training Images come out to be 16000.<br>
For testing the best model, 2000 different images (1000 each of cat and dog) are used out of which 50% (1000) images form the Validation Set. 
The model with the least Validation Loss is saved for future predictions.<br>
The best saved model gives an Accuracy of 89% with a good balance between Precision and Recall.<br><br>
Classification Report - <br>
<p align="center">
<img alt="Confusion Report" width="40%" src="https://github.com/kanakmi/dogvscat/blob/main/confusion_matrix.PNG?raw=True" />
</p>

## About the Model

The Model contains 4 layers of Convolutional Neural Networks with different hyperparameters. Each CNN layer is followed by a MaxPooling2D layer. The second convolutional layer also uses padding to give importance to the features lying in the corners of the images. The dropout layers are added for regularization (to prevent the model from overfitting the training data).<br>
The output from the last Convolutional layer is then Flattened and passed over to a dense Artificial Neural Network containing 4 hidden layers (also some dropout layers) and finally an output layer.<br>
The model has over 5 Million trainable parameters.<br>

### Libraries Required for running the code inside Jupyter Notebook

1. tensorflow 2.3.0 (or above)
2. opencv-python 4.5.2.54
3. scikit-learn 0.24.2
4. matplotlib 3.4.2 (only for visualization)
5. seaborn 0.11.1 (only for visualization)

## UI for the APP

<i>The basic UI for the app is taken from Sports Classifier project made by Dhaval Patel. I have made multiple changes in his code but the html and css file are essentially the same. Link to his Youtube Channel - https://www.youtube.com/channel/UCh9nVJoWXmFb7sLApWGcLPQ</i><br><br>
The <b>server.py</b> file contains the Flask server required to run this app on the system.<br>
The <b>util.py</b> file contains the steps that are performed once the user uploads an image to the app. The saved model is loaded from the memory and input image is preprocessed, predictions are made and the result is routed to the <b>app.js</b> file which maps the output onto the Webpage.<br>

### Libraries Required for GUI & Server -

The required libraries are mentioned in the <b>requirements.txt</b> file inside UI folder and can be simply installed using command <i>pip install requirements.txt</i>

## Steps to Run UI on your system -

1. Download the UI and Trained_Model folder from the repository.
2. Install the required libraries.
3. Run the server.py file and you are ready to go.
