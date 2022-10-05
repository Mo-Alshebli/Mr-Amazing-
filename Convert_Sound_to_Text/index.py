#من الضروري الاتصال بالنت  اثناء تنفيذ  الرنامج 

import speech_recognition as sr
def listen_user():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print('Mr Robot is listening ..')
        audio=rec.listen(source,phrase_time_limit=5)
    try:
        text=rec.recognize_google(audio,language='en_us')
        return text
    except:
        print("Sorry , I had a problem")
        return 0

def connect():
    text_returnd = listen_user()
    print(text_returnd)

connect()
