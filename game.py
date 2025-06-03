import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random as rnd
import os
import time


recognizer = sr.Recognizer()
translator = Translator()

duration = 3
sample_rate = 44100
score = 0

words_by_level = {
    "easy": ["собака", "яблоко", "молоко", "солнце"],
    "average": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}


print("           >>> Добро пожаловать в нашу игру! <<<")
print("      <<< Это игра для проверки уровня англиского >>>")
print(">>> Выберите уровень сложности: легкий - средний - тяжелый <<<")

time.sleep(1)

difficulty = input(">>> Введите сложность: ")
difficulty = translator.translate(difficulty, "en").text

word = rnd.choice(words_by_level[difficulty])

while True:
    print(f"📢 Слово: {word}")

    with sr.Microphone() as source:
        print(">>> Говори <<<")
        audio = recognizer.listen(source, 10, 3)
    
    try:
        
        recognized = recognizer.recognize_google(audio, language="en-US").lower()
        translated = translator.translate(word, "en").text
        
        print("Готово, проверяю🤓")

        print(f"Ты сказал: {recognized}")

        if translated in recognized:
            print("Правильно✅")
            print("+ 1 балл ↑")
            score + 1

        else:
            print(f"Неправильно❌, ты должен был сказать {translated}")
            print("- 1 балл ↓")
            score - 1

        if score <= -3:
            print("Ты проиграл =(")
        break

    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")

    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")

    time.sleep(5)
    os.system("cls")







