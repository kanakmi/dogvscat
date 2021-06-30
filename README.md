# Dog vs Cat

![alt text](https://github.com/kanakmi/dogvscat/blob/main/Cover.png?raw=True)

The classic AI problem to classify images of Cats and Dogs.<br>
The model uses 8000 images (4000 each of Cat and Dog) for the classification task.<br>
The Dataset is Taken from Kaggle and the link for the same is https://www.kaggle.com/chetankv/dogs-cats-images <br>
After Image Augmentation, the total number of Images are 14000 out of which 10% (1400) images form the Validation Set.<br>
The model with least Validation Loss is saved for future predictions.<br>
For testing 2000 different images (1000 each of cat and dog) are used on which the model gives an Accuracy of 82% with a good balance betwwen Precision and Recall.<br>

Libraries Required for running the code inside Jupyter Notebook -
1. tensorflow == 2.3.0 (or above)
2. opencv-python == 4.5.2.54
3. scikit-learn == 0.24.2
4. matplotlib == 3.4.2 (only for visualization)
5. seaborn == 0.11.1 (only for visualization)
