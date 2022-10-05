from gtts import gTTS                                                         
from playsound import playsound                                               
#اكتب النص المراد تحويلة  الى صوت هنا                                                 
mytext="Hello everyone this Welcom in My program "                                        
language='en'                                                                 
myobj=gTTS(text=mytext,lang=language,slow=True)
#سيتم حفظ الصوت في الملف الي في البرنامج
myobj.save("sound.mp3")                                                    
playsound("sound.mp3")                                                     
                                                                              
                                                                              
