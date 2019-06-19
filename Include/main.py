import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')   #https://en.wikipedia.org/wiki/Microsoft_Speech_API
voices = engine.getProperty('voices')

#print(voices)
#print(voices[0].id)
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Assalamu Alikum. Good Morning!")

    elif hour>=12 and hour<18:
        speak("Assalamu Alikum. Good Afternoon!")

    else:
        speak("Assalamu Alikum. Good Evening!")

    speak("I am Istiak Ahmad. Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

email = {"a": "istiakahmad86@gmail.com", "istiak":"istiakahmad86@gmail.com"}

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('istiakahmad86@gmail.com', 'MUHAIMEEN22194')
    server.sendmail('istiakahmad86@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('Searching youtube...')
            query = query.replace("youtube", "")
            webbrowser.open("https://www.youtube.com/"+"results?search_query=" +query)

        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\Song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            for key in email.keys():
                if key in query:
                    try:
                        print("mail to " + email[key])
                        speak("What should I say?")
                        content = takeCommand()
                        to = str(email[key])
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry. I am not able to send this email")
                else:
                    speak("Sorry. mail receiver not found")


