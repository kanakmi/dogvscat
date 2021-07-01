# Dog vs Cat

![alt text](https://github.com/kanakmi/dogvscat/blob/main/Cover.png?raw=True)

The classic AI problem to classify images of Cats and Dogs.<br>
The CNN model uses 8000 images (4000 each of Cat and Dog) for the classification task.<br>
The Dataset is taken from Kaggle and the link for the same is https://www.kaggle.com/chetankv/dogs-cats-images <br>
After Image Augmentation, the total number of Images are 14000 out of which 10% (1400) images form the Validation Set.<br>
The model with the least Validation Loss is saved for future predictions.<br>
For testing the best model, 2000 different images (1000 each of cat and dog) are used on which the model gives an Accuracy of 82% with a good balance between Precision and Recall.<br>

### About the Model -

The Model contains 4 layers of Convolutional Neural Networks with different hyperparameters. Each CNN layer is followed by a MaxPooling2D layer. The second layer also uses padding to give importance to the features visible in the corners of the images. A dropout layer is introduced after the 2nd and 3rd Convolutional layer for regularization (to prevent the model from overfitting the training data).<br>
The output from the last Convolutional layer is then Flattened and passed over to a dense Artificial Neural Network containing 3 hidden layers and finally an output layer.<br>
The model has over 4 Million trainable parameters.

### Libraries Required for running the code inside Jupyter Notebook -

1. tensorflow == 2.3.0 (or above)
2. opencv-python == 4.5.2.54
3. scikit-learn == 0.24.2
4. matplotlib == 3.4.2 (only for visualization)
5. seaborn == 0.11.1 (only for visualization)

## UI for the APP -

<i>The basic UI for the app is taken from Sports Classifier project made by Dhaval Patel. Link to his Youtube Channel - https://www.youtube.com/channel/UCh9nVJoWXmFb7sLApWGcLPQ. </i><br>
The <b>server.py</b> file contains the Flask server required to run this app on the system.
The <b>util.py</b> file contains the steps that are performed once the user uploads an image to the app. The saved model is loaded from the memory and input image is preprocessed, predictions are made and the result is routed to the <b>app.js</b> file which maps the output onto the Webpage.<br>

### Libraries Required for GUI -

1. tensorflow == 2.3.0 (or above)
2. opencv-python == 4.5.2.54
3. Flask == 2.0.1 <br>
<i>There are more libraries mentioned in requirements.txt folder but tensorflow installs most of them automatically.</i>

## Steps to Run this UI on your system -

1. Download the UI folder folder from the repository.
2. Install the required libraries.
3. Download the saved model and model architecture from (https://drive.google.com/drive/folders/1XC1HQtcZplbjjsYw3uzuxQJz448VSuhS?usp=sharing) and paste them in <b>UI</b> folder. <i>*Since GitHub doesn't allows files >25 MB*</i>
4. Run the server.py file and you are ready to go.
