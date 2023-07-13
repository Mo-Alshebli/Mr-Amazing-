
import cv2
def ImhFile():
    img=cv2.imread('12.jpg')
    classnames=[]
    classFile='coco.names'
    with open(classFile,'r')as f:
        print(f)
        classname=f.read().split()
        print(classFile)

        configPAth='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightPAth='frozen_inference_graph.pb'

        net=cv2.dnn_DetectionModel(weightPAth,configPAth)
        net.setInputSize(300,300)
        net.setInputScale(1.0/127.5)
        net.setInputMean(127.5,127.5,127.5)
        net.setInputSwapRB(True)

        classIds,confs,bbox=net.detect(img,confThreshold=0.5)
        print(classIds,bbox,confs)
        for classId,confdence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classnames[classId-1],(box[0]+10,box[1]+20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),thickness=2)

        cv2.imshow("Output",img)
        cv2.waitKey(0)

def Camera():
    cam=cv2.VideoCapture(0)
    classnames = []
    classFile = 'coco.names'
    with open(classFile, 'rt') as f:
        classnames=f.read().rstrip('\n').split('\n')

    configPAth = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightPAth = 'frozen_inference_graph.pb'
    net = cv2.dnn_DetectionModel(weightPAth, configPAth)
    net.setInputSize(300, 300)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    while True:
        success,img=cam.read()
        classIds,confs,bbox=net.detect(img,confThreshold=0.5)
        print(classIds,bbox,confs)

        if len(classIds) !=0:
            for classId, confdence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, classnames[classId - 1], (box[0] + 10, box[1] + 20), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (0, 255, 0), thickness=2)

    cv2.imshow("Output", img)
    cv2.waitKey(0)


Camera()