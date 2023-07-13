import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

# gpus = tf.config.experimental.list_physical_devices('GPU')
# for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu, True)
# tf.config.list_physical_devices('GPU')
# def preprocess_image(image, target_size=(48, 48)):
#     # Convert the image from BGR to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # Resize the image to the target size
#     gray_resized = cv2.resize(gray, target_size)
#     # Normalize the pixel values to be in the range [0, 1]
#     gray_normalized = gray_resized / 255.0
#     # Expand the dimensions of the image to include the channel dimension
#     gray_expanded = np.expand_dims(gray_normalized, axis=-1)
#     return gray_expanded

#
# def load_data(directory, target_size=(48, 48)):
#     images = []
#     labels = []
#
#     for subdir in os.listdir(directory):
#         subdir_path = os.path.join(directory, subdir)
#         if os.path.isdir(subdir_path):
#             label = int(subdir)
#             print(label)
#             for filename in os.listdir(subdir_path):
#                 filepath = os.path.join(subdir_path, filename)
#                 image = cv2.imread(filepath)
#                 preprocessed_image = preprocess_image(image, target_size)
#                 images.append(preprocessed_image)
#                 labels.append(label)
#
#     images = np.array(images)
#     labels = np.array(labels)
#
#     return images, labels
#
#
# def create_model(input_shape, num_classes):
#     model = keras.Sequential([
#         keras.layers.Conv2D(32, (3, 3), input_shape=input_shape),
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
#
#
# # Load the data
# data_directory = 'Data/train'
target_size = (48, 48)
# images, labels = load_data(data_directory, target_size)
# print(len(labels))
# # # # Create the model
# input_shape = (target_size[0], target_size[1], 1)
# print(input_shape)
# num_classes = 8  # The number of classes in your dataset
# model = create_model(input_shape, num_classes)
#
# # # Train the model
# model.fit(images, labels, epochs=40, batch_size=64, validation_split=0.1)
#
# # # Save the model
# model.save('facial_emotion_detection.h5')

# Test the model on a single image
# test_image = cv2.imread('Data/test')
# # print(test_image)
# preprocessed_test_image = preprocess_image(test_image, target_size)
# predictions = model.predict(np.expand_dims(preprocessed_test_image, axis=0))
# predicted_label = np.argmax(predictions)
# print('Predicted emotion:', predicted_label)