import pyttsx3
from win32com.client import Dispatch

def speak_and_print(str):
    print(str.strip())  
    speak(str)  

def speak(str):
    speak=Dispatch(("SAPI.SPVOICE"))
    speak.speak(str)

if __name__== '__main__':
    with open("happy.txt", 'r', encoding='utf=8') as f:
        for item in f.readlines():
            speak_and_print(item)
    
    


        