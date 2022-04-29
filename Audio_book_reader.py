from gtts import gTTS
from playsound import playsound
import os

user = input("Enter the File Name to read it's Audio Book : ")

lines_list = []  # Empty List

with open(f"Books\\{user}.txt") as f:
    for i in range(100):
        lines_list.append(f.readline())

for i in range(len(lines_list)):
    gTTS(text=lines_list[i], lang='en', slow=False).save(
        f"Audio Files\\{user}{i}.mp3")
    playsound(f"Audio Files\\{user}{i}.mp3")
    os.remove(f"Audio Files\\{user}{i}.mp3")
