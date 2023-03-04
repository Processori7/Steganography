## -*- coding: utf-8 -*-

from translate import Translator
from re import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw
from random import randint


def Encrypt():
    translator= Translator(from_lang="ru",to_lang="en")
    keys = []
    print("Выберите картинку\n")
    filename = askopenfilename()
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('keys.txt', 'w')
    text_input = input("Введите текст>>>\n")
    translation_en = translator.translate(text_input)
    print(translation_en)
    for elem in ([ord(elem) for elem in translation_en]):
        key = (randint(1, width - 10), randint(1, height - 10))
        g, b = pix[key][1:3]
        draw.point(key, (elem, g, b))
        f.write(str(key) + '\n',)

    print('Ключ был записан в файл keys.txt, он необходим для расшифровки соощения\n')
    print("Сейчас появиться новая картинка с именем newimage, в которой будет записано послание.\n")
    img.save("newimage.png", "PNG")
    f.close()


def Decrypt():
    translator = Translator(from_lang="en", to_lang="ru")
    a = []
    keys = []
    print("Выберите картинку\n")
    filename = askopenfilename()
    print("Выберите путь к keys.txt\n")
    filename1 = askopenfilename()
    img = Image.open(filename)
    pix = img.load()
    f = open(filename1, 'r', encoding="utf-8")
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'(\d+)\,', y))):
        keys.append((int(findall(r'(\d+)[\,]', y)[i]), int(findall(r'[\,]\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][0])
    message = ''.join([chr(elem) for elem in a])
    print("Ваше сообщение:", translator.translate(message), '\n')



if __name__=='__main__':
    while True:
        b = input("Хотите расшифровать сообщение? Введите 'да' или 'нет' со строчной буквы или введите 'выход' и нажмите Enter>>>")
        b.upper()

        if b =='да':
            Decrypt()
        elif b == 'выход':
            break
        elif b =='нет':
            Encrypt()
        else:
            print('\nКоманда не опознана\n')









