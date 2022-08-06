import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pandas as pq

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyse_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
lefter_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
righter_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')


path='photo'
images=[]
class_name=[]
my_list=os.listdir(path)
for cl in my_list:
    curimg=cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    class_name.append(os.path.splitext(cl)[0])



def find_encoding(images):
    encode_list=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        encode=face_recognition.face_encodings(img)[0]

        encode_list.append(encode)
    return encode_list


def data_base(name):
    with open('data_base.csv','r+') as f:
        my_data_list=f.readlines()
        namelist=[]
        for line in my_data_list:
            entry=line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now=datetime.now()
            detstring=now.strftime('%H:%M:%S')
            f.writelines((f'\n{name},{detstring}'))

encode_listknown=find_encoding(images)


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    faces_curframe = face_recognition.face_locations(imgs)
    encodes_curframe = face_recognition.face_encodings(imgs, faces_curframe)
    for encod_face, face_loc in zip(encodes_curframe, faces_curframe):
        matches = face_recognition.compare_faces(encode_listknown, encod_face)
        face_dis = face_recognition.face_distance(encode_listknown, encod_face)


        matchindex = np.argmin(face_dis)
        if matches[matchindex]:
            name = class_name[matchindex].upper()
            # print(name)
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2),
            data_base(name)
        else:
            unname = 'unknown'
            y1, x2, y2, x1 = face_loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, unname, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow('camar', img)
    k = cv2.waitKey(1)
    if ord('q') == k:
        break




