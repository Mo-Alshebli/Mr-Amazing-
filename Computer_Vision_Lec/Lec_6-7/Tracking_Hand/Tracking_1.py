import cv2
import mediapipe as mp
import time

# print()
cap=cv2.VideoCapture(0)
mphand=mp.solutions.hands
hands=mphand.Hands()
mpDrow=mp.solutions.drawing_utils

ptime=0
ctime=0
while True:
     ret,img=cap.read()

     gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
     result=hands.process(gray)

     if result.multi_hand_landmarks:
          for handlms in result.multi_hand_landmarks:
               for id ,lm in enumerate(handlms.landmark):
                    h, w ,c= img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # if id ==1:
                    cv2.circle(img,(cx,cy),5,(22,111,255),cv2.FILLED)
                    print(cx,cy)



               # print(handlms)
               # print(handlms)

               mpDrow.draw_landmarks(img,handlms,mphand.HAND_CONNECTIONS)

     ctime=time.time()
     fps=1/(ctime-ptime)
     ptime=ctime

     cv2.putText(img,f"fps : {str(int(fps))}",(30,30),cv2.FONT_HERSHEY_PLAIN,3,(0,222,202),2)
     cv2.imshow("Image",img)
     if cv2.waitKey(1) == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()