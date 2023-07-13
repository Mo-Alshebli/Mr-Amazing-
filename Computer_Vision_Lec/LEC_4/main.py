import cv2
import mediapipe as mp
image=cv2.imread('person.jpg')
mp_face_mesh=mp.solutions.face_mesh.FaceMesh()
rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
result=mp_face_mesh.process(rgb_image)
height,width,_=image.shape
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0,468):
        pt1=facial_landmarks.landmark[i]
        print(pt1)
        x=int(pt1.x*width)
        y=int(pt1.y*height)
        cv2.circle(image,(x,y),2,(100,100,0),-1)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# mp_face_mesh=mp.solutions.face_mesh.FaceMesh()
# cap=cv2.VideoCapture(0)
# while True:
#     ret,image=cap.read()
#     if ret is not True:
#         break
#     height, width, _ = image.shape
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     result = mp_face_mesh.process(rgb_image)
#     for facial_landmarks in result.multi_face_landmarks:
#         for i in range(0, 468):
#             pt1 = facial_landmarks.landmark[i]
#             print(pt1)
#             x = int(pt1.x * width)
#             y = int(pt1.y * height)
#             cv2.circle(image, (x, y), 2, (200, 250, 220), -1)
#     cv2.imshow("Image", image)
#     k=cv2.waitKey(1)
#     if k==27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()
