from gtts import gTTS                                                         
from playsound import playsound                                               
#اكتب النص المراد تحويلة  الى صوت هنا                                                 
mytext="welcome my student in artifical intelligence  how are you ?" \        
       "you are best student "                                                
language='en'                                                                 
myobj=gTTS(text=mytext,lang=language,slow=True)
#سيتم حفظ الصوت في الملف الي في البرنامج
myobj.save("welcome1.mp3")                                                    
playsound("welcome1.mp3")                                                     
                                                                              
                                                                              
