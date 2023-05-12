# import the necessary libraries
from deepface import DeepFace
import cv2

# define a function to detect face in the image
def detect(img):
    text=0
    # try to analyze the image and detect face
    try:
        # DeepFace.analyze() function returns a dictionary of results which include face detection information
        result = DeepFace.analyze(img, actions=["detect"])
        face_=[]
        # loop over the face detection results and extract the region of interest (ROI)
        for face in result[0]["region"]:
            face_.append(result[0]["region"][face])
        # get the ROI coordinates
        (x,y,w,h)=face_
        # draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 50), 3)
    except:
        # if no face is detected set a flag text=1
        text=1

    # return the image and the flag
    return img,text

# define a function to analyze the image for age, gender, and emotion
def deepface_age_gender_emotion(data):
    # get the dominant gender, age, and emotion
    gender=data[0]['dominant_gender']
    age=data[0]['age']
    emotion=data[0]["dominant_emotion"]

    # return the gender, age, and emotion
    return gender,age,emotion

# main function to capture the video from the webcam and process it for face detection and recognition
def main():
    # create a VideoCapture object to capture video from the default camera
    cap = cv2.VideoCapture(0)
    data=""
    # start the loop to capture the video and process it in real-time
    while True:
        # read the frame from the camera
        ret,frame=cap.read()
        # define the font to use for text annotations
        font = cv2.FONT_HERSHEY_SIMPLEX
        # detect the face in the frame using the detect() function
        img,text=detect(frame)
        # check if face is detected or not, if not print a message on the frame
        if text==1:
            cv2.putText(frame,"No face detection ",(50,50),font,1,(10,100,230),2)
        else:
            try:
                # analyze the image for age, gender, and emotion
                objs = DeepFace.analyze(img_path=frame,actions=['age', 'gender', 'emotion'])
                # extract the relevant information from the analysis results
                data = deepface_age_gender_emotion(objs)
            except:
                pass
            # display the age, gender, and emotion on the frame
            cv2.putText(frame,str(data),(30,30),font,0.5,(10,100,230),1)

        # display the original video with annotations
        cv2.imshow("Original video ",frame)

        # check if the user has pressed the 'q' key, if yes then exit the loop
        if cv2.waitKey(1)=='q':
            break

    # release the camera object and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

# call the main function
if __name__ == "__main__":
    main()
