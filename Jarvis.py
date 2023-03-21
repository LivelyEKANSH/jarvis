import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir.")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir.")
    elif hour>=18 and hour <24:
        speak("Good evening sir.")
    else:
        speak("Good night sir.")
    speak("Jarvis at your service, please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return"None"
    return query


def wiki(query):
    speak("Searching...")
    query = query.replace("wikipedia","")
    result = wikipedia.summary(query, sentences = 2)
    print(result)
    speak(result)


def sendMail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',5674)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','1234')
    server.sendmail('ekanshtanwar@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            wiki(query)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                speak("To who should i send the email?")
                to = takeCommand()
                sendMail(to,content)
                speak("email has been sent successfully")
                speak("the content of the email were")
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send email")
        
        elif 'search in chrome' in query:
            speak("what should i search?")
            chromePath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' or 'play music' in query:
            songs_dir = "D:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'offline' in query:
            quit()
        
