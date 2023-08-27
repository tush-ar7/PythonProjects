#import os


# if __name__ == '__main__':
#     print("Welcome to robo speaker ... Created by Luffy")
#     while True:
#         x = input("Enter what you want to speak:")
#         if (x == "q"):
#             break
#         command = f" say {x} "
#         os.system(command)
# import os
#
# if __name__ =="_main__":
#     print("Welcome")
#     while(True):
#         s=input("Say it: ")
#         if(s=="q"):
#            break
#
#         command=f"PowerShell -Command Add-Type -AssemblyNameSystem.Speech;(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
#
# os.system(command)
import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while(True):
        word = input("Enter your command: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()