import cv2
import numpy as np

ww=50
hh=50
offset=4
y1=300
delay=60
detec=[]
carros=0

def page_center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy


cap = cv2.VideoCapture("Relaxing highway traffic.mp4")
print(cap.get(3), cap.get(4))
BGS = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    img_sub = BGS.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    contor, h = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.line(frame1, (20, y1), (570, y1), (123, 230, 0), 2)
    for (i, c) in enumerate(contor):
        (x, y, w, h) = cv2.boundingRect(c)

        validar_contorno = (w >= ww) and (h >= hh)
        if not validar_contorno:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, h + y), (0, 255, 0), 2)
        center = page_center(x, y, w, h)
        detec.append(center)
        cv2.circle(frame1, center, 4, (11, 11, 255), -1)

        for (x, y) in detec:
            if (y < (y1 + offset)) and (y > (y1 - offset)):
                carros += 1
                cv2.line(frame1, (25, y1), (540, y1), (1, 30, 220), 5)
                detec.remove((x, y))
                print(" Number of Cars detect : " + str(carros))
    cv2.putText(frame1, "Count : " + str(carros), (20, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (20, 20, 12), 2)
    cv2.imshow("Video original ", frame1)
    cv2.imshow("dilat", dilat)
    cv2.imshow("img_sub", img_sub)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
cap.release()