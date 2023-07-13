import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from PIL import Image

import cv2
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
tf.config.list_physical_devices('GPU')
def preprocess_image(image, target_size=(256,256)):
    # Convert the image from BGR to grayscale
    # cv2.imshow("nn",image)
    # cv2.waitKey(0)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resize the image to the target size

    # OUTPUT>>> (2000, 1700)
    resized_image = image.resize((200, 200))
    # gray_resized = cv2.resize(image, target_size)
    # Normalize the pixel values to be in the range [0, 1]
    # gray_normalized = image / 255
    # Expand the dimensions of the image to include the channel dimension
    gray_expanded = np.expand_dims(resized_image, axis=-1)
    return gray_expanded


def load_data(directory, target_size=(256,256)):
    images = []
    labels = []

    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            label = int(subdir)
            print(label)
            for filename in os.listdir(subdir_path):
                filepath = os.path.join(subdir_path, filename)
                # image = cv2.imread(filepath)
                print(filepath)
                image=Image.open(filepath)
                preprocessed_image = preprocess_image(image, target_size)
                images.append(preprocessed_image)
                labels.append(label)

    images = np.array(images)
    labels = np.array(labels)

    return images, labels


# def create_model(input_shape, num_classes):
#     model = keras.Sequential([
#         keras.layers.Conv2D(32, (3, 3), input_shape=(200,200,3)),
#         keras.layers.MaxPooling2D((2, 2)),
#         keras.layers.Conv2D(64, (3, 3), activation='relu'),
#         keras.layers.MaxPooling2D((2, 2)),
#         keras.layers.Flatten(),
#         keras.layers.Dropout(0.5),
#         keras.layers.Dense(128, activation='relu'),
#         keras.layers.Dense(num_classes, activation='softmax')
#     ])
#     model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
#     return model

def create_model(input_shape, num_classes):
    emotion_model = Sequential()

    emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(200, 200, 3)))
    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))

    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))

    emotion_model.add(Flatten())
    emotion_model.add(Dense(128, activation='relu'))
    emotion_model.add(Dropout(0.5))
    emotion_model.add(Dense(num_classes, activation='softmax'))

    # cv2.ocl.setUseOpenCL(False)

    # emotion_model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.0001, decay=1e-6), metrics=['accuracy'])

    emotion_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return emotion_model

# Load the data
data_directory = 'fu/T'
target_size = (200, 200)
images, labels = load_data(data_directory, target_size)
print(labels)
# from sklearn.preprocessing import MinMaxScaler
# minmax=MinMaxScaler(feature_range=(0,1))
# images=minmax.fit_transform(images)
# print(np.unique(labels))
# # # Create the model
input_shape = (target_size[0], target_size[1], 1)
# print(input_shape)
num_classes = 21  # The number of classes in your dataset
model = create_model(input_shape, num_classes)
# #
# model.summry
# # # Train the model
model.fit(images, labels, epochs=75, batch_size=64,validation_split=0.1)
#
# # Save the model
model.save('hand.h5')
# Test the model on a single image
# test_image = cv2.imread('Data/test/1/PrivateTest_88305.jpg')
# print(test_image)
# preprocessed_test_image = preprocess_image(test_image, target_size)
# data_directory = 'Data/test'
# images, labels = load_data(data_directory, target_size)
#
# model = load_model('Emotion_detection_with_CNN-main/model/emotion_model.h5')
# predictions = model.predict(images)
# predicted_label=[]
# # print('Predicted emotion:',np.argmax(predictions))
#
# for i in predictions:
#     predicted_label.append(np.argmax(i))
#
# print(len(labels),len(predicted_label))
# re=0
# r=0
# g=0
# for i in range(len(labels)):
#
#
#     if labels[i]==predicted_label[i]:
#         # print(labels[i],predicted_label[i])
#         re=re+1
#     else:
#         r=r+1
#
#
# print(re,r)