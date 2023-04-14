import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia
import smtplib
import webbrowser as wb     

engine= pyttsx3.init()                          #initialization
voices= engine.getProperty('voices')            #gets different voices
engine.setProperty('voice', voices[1].id)       #female voice
newVoiceRate= 190                               #voice rate
engine.setProperty('rate', newVoiceRate) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():                                      #time function
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

def date():                                      #date function
 year   = int(datetime.datetime.now().year)
 month  = int(datetime.datetime.now().month)
 day    = int(datetime.datetime.now().day)
 speak("Current date is ")
 speak(day)
 speak(month)
 speak(year)
   
def wishme():                                     #wish function
       
       hour = datetime.datetime.now().hour

       if hour >= 6 and hour < 12:
        speak("Good morning Sir")

       elif hour >=12 and hour < 17:
        speak("Good afternoon Sir")
       elif hour >= 17 and hour < 24:
        speak("Good evening Sir")
       else :  speak("Good night")


       speak("Hazel at your service. How can I help you")


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source) 
 
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language= "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Can you repeat that again please!")
     
        return "None"
    
    return query

def sendmail(to,content):
    server = smtplib.smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.login("test@gmail.com","123test")
    server.sendmail("text@gmail.com",to,content)
    server.close()



if __name__=="__main__":
 wishme()

 while True:
          query=takeCommand().lower()
          print(query)

          if "time" in query:
              time()
           
          elif "date" in query:
              date()
        
          elif "offline" in query:
              quit()    

          elif "wikipedia" in query:
              speak("searching...")
              query= query.replace("wikipedia", "")
              result=wikipedia.summary(query,sentences=2)
              speak(result)
          
          elif "send email" in query:
              try:
                  speak("What should I say?")
                  content = takeCommand()
                  to = "xyz@gmail.com"
                  sendmail(to, content)
                  speak("content")
             
              except Exception as e:
                  speak(e)
                  speak("Unable to send the mail")

          elif "search in firefox" in query:
                speak("What should I search?")
                morzillapath = "C:\Program Files (x86)\Mozilla Firefox %s"
                search = takeCommand().lower()
                wb.get(morzillapath).open_new_tab(search + ".com")

