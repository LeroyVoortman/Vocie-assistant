# imports
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
import pyautogui


# initialise a recogniser
r = sr.Recognizer()



# record voice and convert it to text
def record_voice(ask=False):
    with sr.Microphone() as source:
        

        if ask:
            assistand_speak(ask)
        audio = r.listen(source,)
        voice_input = ''
        try:
            voice_input = r.recognize_google(audio)
        except sr.UnknownValueError:
            assistand_speak('Sorry, i did not get that.')
        except sr.RequestError:
            assistand_speak('Sorry, i am not able to do that yet.')
        return voice_input

#makes assistant speak
def assistand_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

#Response on given task
def respond(voice_input):
    if 'what is your name' in voice_input:
        assistand_speak('My name is Azazel')
    if 'what time is it' in voice_input:
        assistand_speak(ctime())
    if 'search' in voice_input:
        search = record_voice('What can i search for you?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        assistand_speak('This is what i found for ' + search)
    if 'find location' in voice_input:
        location = record_voice('What is the location you are looking for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        assistand_speak('Here is the location you asked for ' + location)
    if 'scare me' in voice_input:
        url = 'https://www.youtube.com/watch?v=-1dSY6ZuXEY&t=12s'
        webbrowser.get().open(url)
        assistand_speak('Okay you asked for it...')
    if 'play music' in voice_input:
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.get().open(url)
        assistand_speak('Get rick rolled noob!')
    if 'open' in voice_input:
        pyautogui.press('win')
        open = record_voice('Which application do you want to open?')
        pyautogui.typewrite(open)
        pyautogui.press('enter')
        assistand_speak("No problem sir i will open it for you!")
    if 'exit' in voice_input:
        assistand_speak("Alright sir, i'm here for you if you need me again.")
        exit()

#when running always listen for next command
time.sleep(1)
assistand_speak('Good day sir, How can i help you?')
while 1:
    voice_input = record_voice()
    respond(voice_input)


