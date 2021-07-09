import numpy as np
import cv2
import tensorflow as tf
import os
import base64

with open('../Trained_Model/DogvsCat-model.json', 'r') as json_file:
    json_savedModel = json_file.read()

# load the model architecture
model = tf.keras.models.model_from_json(json_savedModel)
model.load_weights('../Trained_Model/DogvsCat_weights.hdf5')
model.compile(optimizer="Adam",loss="sparse_categorical_crossentropy", metrics=["accuracy"])

labels = {0: "cat", 1: "dog"}
class_dict = {"cat":0, "dog":1}

def get_cv2_image_from_base64_string(b64str):
    '''
    credit: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    :param uri:
    :return:
    '''
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def classify_image(file_path):
    img = get_cv2_image_from_base64_string(file_path)
    img = cv2.resize(img,(96,96))
    img = np.array(img)
    img = img/255
    img = img.reshape((1, 96, 96, 3))
    predictions = model.predict(img)

    result = []

    result.append({
        'class': labels[np.argmax(predictions[0])],
        'class_probability': np.round(predictions*100,2).tolist()[0],
        'class_dictionary': class_dict
    })
    print(result)
    return result