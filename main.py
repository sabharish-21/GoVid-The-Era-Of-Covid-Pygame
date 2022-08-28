import math
import random
import pygame
from pygame import mixer
from tkinter import *
import imageio
from tkinter import Tk, Label
from PIL import ImageTk, Image
import pygame.mixer as m
import time
import sys
import webbrowser
import pickle as p

# Video
m.init()
video_name = 'Video//anime.mp4'
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])


def stream(label):
    try:
        image = video.get_next_data()
    except:
        video.close()
        return
    label.after(delay, lambda: stream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image


if __name__ == '__main__':
    root = Tk()
    root.geometry("640x352")
    my_label = Label(root)
    my_label.pack()
    my_label.after(delay, lambda: stream(my_label))
    m.music.load('Video//anime.mp3')
    m.music.play()
    root.after(90000, lambda: root.destroy())
    root.mainloop()
    m.music.stop()

# Main Program

pygame.init()
mixer.init()
file = open("Log//score.txt", "a+")
screen = pygame.display.set_mode((800, 600))

# Background Bgm and Image
background = pygame.image.load('Icons//bg.png')
m.music.stop()
m.music.load('Audio//intro.wav')
m.music.set_volume(0.3)
m.music.play(-1)


# Caption and Icon
pygame.display.set_caption("GO-VID - The Era Of COVID")
icon = pygame.image.load('Icons//player.png')
pygame.display.set_icon(icon)

# Player
d = 8
playerImg = pygame.image.load('Icons//d{}.png'.format(d))
playerX = 0
playerY = 270
playerY_change = 0
playerX_change = 0

# Virus
virus_count = 6
vchange_Y = []
vchange_X = []
virusimg = []
vX = []
vY = []
vimg_1 = pygame.image.load('Icons/virus.png')
vimg_2 = pygame.image.load('Icons/v.png')
virus_e = [vimg_1, vimg_2]


def inc_virus():
    global virus_e
    vchange_X.clear()
    vchange_Y.clear()
    virusimg.clear()
    vX.clear()
    vY.clear()
    for i in range(virus_count):
        virusimg.append(random.choice(virus_e))
        vX.append(random.randint(400, 700))
        vY.append(random.randint(0, 536))
        vchange_X.append(60)
        vchange_Y.append(0.3)

inc_virus()

# Bullet
bulletImg = pygame.image.load('Icons//water.png')
bulletX = 0
bulletY = 0
bulletX_change = 5
bulletY_change = 0
bullet_state = "ready"
kill_value = 0

# Score
score_val = 0
var_score = 10

# Power Up
s_i = 1
sanitizer = 0
simg = pygame.image.load("Icons//s{}.png".format(s_i))
sx = random.randint(0, 736)
sy = random.randint(0, 536)
schange_x = 0
schange_y = 0.3
power = 0
font = pygame.font.Font('freesansbold.ttf', 23)
l = 0
# score co ordinates
sc_x = 5
sc_y = 75
# power co ordinates
po_x = 0
po_y = 40
sh_x = 5
sh_y = 10
state = False
st_t = pygame.font.Font('freesansbold.ttf', 23)
st_o = pygame.font.Font('freesansbold.ttf', 23)
a = 0
show_b = False
file_coin = open('Log//coins.txt', 'r+')
file_coin.seek(0)
coin = int(file_coin.read())
file_coin.seek(0)
price = [100, 200, 300, 400, 500, 600, 700, 0]
price1 = [0, 500, 1000, 1500]

file_shop = []
y = 0


# Shop
def shop():
    global background, pos, show_s, show_b, show, coin, d, simg, playerImg, s_i, file_shop, y, file_coin
    d_x = 10
    d_y = 100
    s_x = 10
    s_y = 400
    if show_s:
        background = pygame.image.load("Icons//bg 2.png")
        txt1 = st_o.render('BACK', True, (255, 255, 255))
        screen.blit(txt1, (10, 15))
        pygame.draw.rect(screen, (255, 255, 255), (0, 5, 100, 40), 4)
        txt2 = st_o.render(str(coin), True, (255, 255, 255))
        screen.blit(txt2, (660, 10))
        ti = pygame.image.load("Icons//coin.png")
        screen.blit(ti, (620, 10))
        txt12 = st_o.render('DRONES', True, (255, 255, 255))
        screen.blit(txt12, (350, 50))
        for i in range(1, 9):
            ti1 = pygame.image.load("Icons//d{}.png".format(i))
            screen.blit(ti1, (d_x, d_y))
            s_p = open("Log//shop.dat", 'rb')
            s_p.seek(0)
            file_shop = p.load(s_p)

            if i in file_shop['drone_store'] and i != d:
                txt124 = st_o.render('USE', True, (255, 255, 255))
                screen.blit(txt124, (d_x, d_y + 90))
                pygame.draw.rect(screen, (255, 255, 255), (d_x - 10, d_y + 80, 70, 40), 4)

            if i != d and i not in file_shop['drone_store'] and file_shop['drone'] != i:
                txt124 = st_o.render('BUY', True, (255, 255, 255))
                screen.blit(txt124, (d_x, d_y + 90))
                pygame.draw.rect(screen, (255, 255, 255), (d_x - 10, d_y + 80, 70, 40), 4)
                txt124 = st_o.render(str(price[i - 1]), True, (255, 255, 255))
                screen.blit(txt124, (d_x, d_y + 150))
                ti = pygame.image.load("Icons//coin.png")
                screen.blit(ti, (d_x + 50, d_y + 150))
            if d == i:
                pygame.draw.rect(screen, (255, 255, 255), (d_x - 10, d_y + 80, 70, 40), 4)
                txt124 = st_o.render('USED', True, (255, 170, 29))
                screen.blit(txt124, (d_x - 5, d_y + 90))

            d_x += 100
        txt123 = st_o.render('SANITIZERS', True, (255, 255, 255))
        screen.blit(txt123, (345, 350))
        for i in range(1, 5):
            ti2 = pygame.image.load("Icons//s1{}.png".format(i))
            screen.blit(ti2, (s_x, s_y))
            s_p = open("Log//shop.dat", 'rb')
            s_p.seek(0)
            file_shop = p.load(s_p)
            if file_shop['san'] == i and s_i == i:
                pygame.draw.rect(screen, (255, 255, 255), (s_x - 10, s_y + 80, 70, 40), 4)
                txt1234 = st_o.render('USED', True, (255, 170, 29))
                screen.blit(txt1234, (s_x - 5, s_y + 90))

            elif i in file_shop['san_store']:
                txt1234 = st_o.render('USE', True, (255, 255, 255))
                screen.blit(txt1234, (s_x, s_y + 90))
                pygame.draw.rect(screen, (255, 255, 255), (s_x - 10, s_y + 80, 70, 40), 4)

            elif (s_i != i):
                txt1234 = st_o.render('BUY', True, (255, 255, 255))
                screen.blit(txt1234, (s_x, s_y + 90))
                pygame.draw.rect(screen, (255, 255, 255), (s_x - 10, s_y + 80, 70, 40), 4)
                txt1234 = st_o.render(str(price1[i - 1]), True, (255, 255, 255))
                screen.blit(txt1234, (s_x, s_y + 150))
                ti = pygame.image.load("Icons//coin.png")
                screen.blit(ti, (s_x + 50, s_y + 150))
            s_x += 100
        if len(pos) > 0:
            for i in range(0, 100):
                for j in range(5, 45):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            show = False
                            show_s = False
                            show_b = False
                            st()

            # DRONE
            for i in range(0, 70):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 1
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                            elif y in file_shop['drone_store']:
                                d = y
                                s_p = open("Log//shop.dat", 'rb+')
                                s_p.seek(0)
                                file_shop["drone"] = d
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                                show_s = True
                                show = False
                                show_b = False
            for i in range(100, 170):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 2
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                            elif y in file_shop['drone_store']:
                                d = y
                                s_p = open("Log//shop.dat", 'rb+')
                                s_p.seek(0)
                                file_shop["drone"] = d
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                                show_s = True
                                show = False
                                show_b = False
            for i in range(200, 270):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 3
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                        elif y in file_shop['drone_store']:
                            d = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["drone"] = d
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                            show_s = True
                            show = False
                            show_b = False
            for i in range(300, 370):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 4
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                        elif y in file_shop['drone_store']:
                            d = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["drone"] = d
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                            show_s = True
                            show = False
                            show_b = False
            for i in range(400, 470):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 5
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                            elif y in file_shop['drone_store']:
                                d = y
                                s_p = open("Log//shop.dat", 'rb+')
                                s_p.seek(0)
                                file_shop["drone"] = d
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                                show_s = True
                                show = False
                                show_b = False
            for i in range(500, 570):
                for j in range(180, 220):
                    if pos[0] == i and pos[1] == j:
                        if show_b:
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_name = p.load(s_p)
                            s_p.seek(0)
                            y = 6
                            if y not in file_name['drone_store']:
                                if price[y - 1] <= coin:
                                    coin -= price[y - 1]
                                    file_coin.write(str(coin))
                                    file_coin.flush()
                                    file_coin.seek(0)
                                    file_shop['drone_store'].append(y)
                                    s_p.seek(0)
                                    p.dump(file_shop, s_p)
                                    s_p.flush()
                                    s_p.seek(0)
                                    show_s = True
                                    show = False
                                    show_b = False

                        elif y in file_shop['drone_store']:
                            d = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["drone"] = d
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                            show_s = True
                            show = False
                            show_b = False
        for i in range(600, 670):
            for j in range(180, 220):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 7
                        if y not in file_name['drone_store']:
                            if price[y - 1] <= coin:
                                coin -= price[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['drone_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False

                    elif y in file_shop['drone_store']:
                        d = y
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_shop["drone"] = d
                        p.dump(file_shop, s_p)
                        s_p.flush()
                        s_p.seek(0)
                        playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                        show_s = True
                        show = False
                        show_b = False
        for i in range(700, 770):
            for j in range(180, 220):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 8
                        if y not in file_name['drone_store']:
                            if price[y - 1] <= coin:
                                coin -= price[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['drone_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False
                        if y in file_shop['drone_store']:
                            d = y
                            s_p.seek(0)
                            s_p = open("Log//shop.dat", 'rb+')
                            file_shop["drone"] = d
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            playerImg = pygame.image.load('Icons//d{}.png'.format(d))
                            show_s = True
                            show = False
                            show_b = False

        # SANI
        for i in range(0, 70):
            for j in range(480, 520):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 1
                        if y not in file_name['san_store']:
                            if price1[y - 1] <= coin:
                                coin -= price1[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['san_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False

                        elif y in file_shop['san_store']:
                            s_i = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["san"] = s_i
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            simg = pygame.image.load('Icons//s1{}.png'.format(s_i))
                            show_s = True
                            show = False
                            show_b = False
        for i in range(100, 170):
            for j in range(480, 520):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 2
                        if y not in file_name['san_store']:
                            if price1[y - 1] <= coin:
                                coin -= price1[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['san_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False

                        elif y in file_shop['san_store']:
                            s_i = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["san"] = s_i
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            simg = pygame.image.load('Icons//s1{}.png'.format(s_i))
                            show_s = True
                            show = False
                            show_b = False
        for i in range(200, 270):
            for j in range(480, 520):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 3
                        if y not in file_name['san_store']:
                            if price1[y - 1] <= coin:
                                coin -= price1[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['san_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False

                        elif y in file_shop['san_store']:
                            s_i = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["san"] = s_i
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            simg = pygame.image.load('Icons//s1{}.png'.format(s_i))
                            show_s = True
                            show = False
                            show_b = False
        for i in range(300, 370):
            for j in range(480, 520):
                if pos[0] == i and pos[1] == j:
                    if show_b:
                        s_p = open("Log//shop.dat", 'rb+')
                        s_p.seek(0)
                        file_name = p.load(s_p)
                        s_p.seek(0)
                        y = 4
                        if y not in file_name['san_store']:
                            if price1[y - 1] <= coin:
                                coin -= price1[y - 1]
                                file_coin.write(str(coin))
                                file_coin.flush()
                                file_coin.seek(0)
                                file_shop['san_store'].append(y)
                                s_p.seek(0)
                                p.dump(file_shop, s_p)
                                s_p.flush()
                                s_p.seek(0)
                                show_s = True
                                show = False
                                show_b = False

                        elif y in file_shop['san_store']:
                            s_i = y
                            s_p = open("Log//shop.dat", 'rb+')
                            s_p.seek(0)
                            file_shop["san"] = s_i
                            p.dump(file_shop, s_p)
                            s_p.flush()
                            s_p.seek(0)
                            simg = pygame.image.load('Icons//s1{}.png'.format(s_i))
                            show_s = True
                            show = False
                            show_b = False


# co ordinates of ballon

y_pos = 550
y_ch = 0
b_show = False


def ballon(y):
    global y_pos
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (100, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (200, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (300, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (400, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (500, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (600, int(y)))
    ti = pygame.image.load("Icons//ballons.png")
    screen.blit(ti, (700, int(y)))

g_show=False
# scores
def score_page():
    global background, a, j, file, score_val, pos, running, game_over, end, state, var_score, power, n, l,gobackmusic
    global y_pos, b_show, show_s,show_b,show,g_show,state,turn

    a = 1
    j = 0
    if not g_show:
        file = open("Log//score.txt", "a+")
        background = pygame.image.load("Icons//bg1.png")
        tx = score_font.render('SCORE : ' + str(score_val), True, (255, 255, 255))
        screen.blit(tx, (300, 100))
        nx = score_font.render('VIRUS KILLED : ' + str(kill_value), True, (255, 255, 255))
        screen.blit(nx, (300, 150))
        pygame.draw.rect(screen, (255, 255, 255), (250, 190, 100, 35), 4)
        txt = score_font.render('  QUIT ', True, (255, 255, 255))
        screen.blit(txt, (255, 195))
        we = pygame.image.load("Icons//criss-cross.png")
        screen.blit(we, (210, 190))
        pygame.draw.rect(screen, (255, 255, 255), (400, 190, 200, 35), 4)
        txt = score_font.render('  PLAY AGAIN ', True, (255, 255, 255))
        screen.blit(txt, (410, 195))
        y = pygame.image.load("Icons//replay.png")
        screen.blit(y, (610, 190))
        t = st_t.render('GO HOME', True, (255, 255, 255))
        screen.blit(t, (20, 20))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, 130, 40), 4)


        if len(pos) > 0:
            for i in range(250, 350):
                for j in range(190, 225):
                    if pos[0] == i and pos[1] == j:
                        pygame.draw.rect(screen, (255, 50, 0), (250, 190, 100, 35))
                        txt = score_font.render('  QUIT ', True, (255, 255, 255))
                        screen.blit(txt, (255, 195))
                        if show:
                            running = False
                            b_show = False
                            show_s = False
                            store()
                            sys.exit()
            for i in range(400, 600):
                for j in range(190, 225):
                    if pos[0] == i and pos[1] == j:
                        pygame.draw.rect(screen, (173, 216, 230), (400, 190, 200, 35))
                        txt = score_font.render('  PLAY AGAIN ', True, (255, 255, 255))
                        screen.blit(txt, (410, 195))
                        if show:
                            store()
                            b_show = False
                            game_over = False
                            end = False
                            state = True
                            gobackmusic=False
                            score_val = 0
                            var_score = 0
                            power = 0
                            n = 0
                            l = 0
                            turn=1
                            bg()
                            inc_virus()
                            playagain()
            for i in range(10, 140):
                for j in range(10, 50):
                    if pos[0] == i and pos[1] == j:
                         if show:
                           store()
                           game_over = False
                           end = False
                           turn=False
                           score_val = 0
                           var_score = 0
                           power = 0
                           n = 0
                           l = 0
                           b_show = False
                           gobackmusic=True
                           show = False
                           show_s = False
                           show_b=False
                           g_show=True
                           state=False
                           st()
        file = open("Log//score.txt", "r")
        z = file.readlines()
        if len(z) == 0:
            b_show = True
            t = st_o.render('HIGH SCORE!!!!', False, (255, 255, 255))

            m.Sound("Audio//highscore.wav").play()
            gobackmusic = True
            screen.blit(t, (300, 50))
            ty = pygame.image.load("Icons//new.png")
            screen.blit(ty, (480, 30))
            ta = pygame.image.load("Icons//confetti (2).png")
            screen.blit(ta, (690, 250))
            ta1 = pygame.image.load("Icons//confetti (21).png")
            screen.blit(ta1, (-30, 250))
            ballon(y_pos)



        if len(z) >= 1:
            s = max(z)
            s = s.rstrip()
            if int(s) < score_val:
                b_show = True
                t = st_o.render('HIGH SCORE!!!!', False, (255, 255, 255))
                gobackmusic = True
                m.Sound("Audio//highscore.wav").play()
                screen.blit(t, (300, 50))
                ty = pygame.image.load("Icons//new.png")
                screen.blit(ty, (480, 30))
                ta = pygame.image.load("Icons//confetti (2).png")
                screen.blit(ta, (690, 250))
                ta1 = pygame.image.load("Icons//confetti (21).png")
                screen.blit(ta1, (-30, 250))
                ballon(y_pos)


# play again
def playagain():
    global sc_y, sh_y, sh_x, sc_x, po_y, po_x, sx, sy, playerX, playerY, b_show, y_pos, y_ch
    sc_x = 5
    sc_y = 75
    po_x = 0
    po_y = 40
    sh_x = 5
    sh_y = 10
    sx = random.randint(0, 736)
    sy = random.randint(0, 536)
    playerX = 0
    playerY = 270
    b_show = False
    y_pos = 550
    y_ch = 0


pos = ()
show = False
show_s = False
gobackmusic=False

# STARTING TXT
def st():
    global pos, game_time, show, show_s, show_b, background, turn,state,game_over,end,score_val,var_score,power,n,l,g_show,gobackmusic
    show_b = False
    background = pygame.image.load('Icons//bg.png')


    if not show_s:

        t = st_t.render('Enter The Game ', True, (255, 255, 255))
        screen.blit(t, (310, 340))
        pygame.draw.rect(screen, (255, 255, 255), (250, 330, 300, 40), 4)
        t = st_t.render('SHOP', True, (255, 255, 255))
        screen.blit(t, (705, 20))
        pygame.draw.rect(screen, (255, 255, 255), (690, 10, 100, 40), 4)
        z = pygame.image.load("Icons//cart.png")
        screen.blit(z, (620, 1))
        pygame.draw.rect(screen, (255, 255, 255), (250, 330, 300, 40), 4)
        t = st_t.render('OUR LINK', True, (255, 255, 255))
        screen.blit(t, (675, 75))
        pygame.draw.rect(screen, (255, 255, 255), (660, 68, 140, 40), 4)
        z = pygame.image.load("Icons//chrome.png")
        screen.blit(z, (620, 71))

        if len(pos) > 0 and not state:
            for i in range(250, 551):
                for j in range(330, 370):
                    if pos[0] == i and pos[1] == j:

                        pygame.draw.rect(screen, (255, 255, 255), (250, 330, 300, 40))

                        pygame.draw.rect(screen, (255, 182, 0), (250, 330, 150, 40))
                        pygame.draw.rect(screen, (0, 0, 0), (250, 330, 300, 40), 4)
                        t = st_t.render('Enter The Game ', True, (0, 0, 0))
                        screen.blit(t, (300, 340))
                        if show:
                            game_time = int(time.process_time())
                            turn = 1
                            state=True
                            game_over = False
                            game_over = False
                            end = False
                            state = True
                            score_val = 0
                            var_score = 0
                            power = 0
                            n = 0
                            l = 0
                            g_show=False
                            inc_virus()
                            playagain()
                            bg()

        if len(pos) > 0 and not state:
            for i in range(690, 790):
                for j in range(15, 55):
                    if pos[0] == i and pos[1] == j:
                        pygame.draw.rect(screen, (255,170,29), (690, 10, 100, 40))
                        pygame.draw.rect(screen, (255, 255, 255), (690, 10, 100, 40), 4)
                        t = st_t.render('SHOP', True, (255, 255, 255))
                        screen.blit(t, (705, 20))
                        if show:
                            show_s = True
                            show = False
                            shop()

        if len(pos) > 0 and not state:
            for i in range(660, 790):
                for j in range(68, 108):
                    if pos[0] == i and pos[1] == j:

                        pygame.draw.rect(screen, (255,170,29), (660, 68, 140, 40))
                        t = st_t.render('OUR LINK', True, (255, 255, 255))
                        screen.blit(t, (675, 75))
                        pygame.draw.rect(screen, (255, 255, 255), (660, 68, 140, 40), 4)
                        z = pygame.image.load("Icons//chrome.png")
                        screen.blit(z, (620, 71))
                        if show:
                            show = False
                            webbrowser.open("https://lethalgames.pythonanywhere.com/")


# storing in txt file
def store():
    file = open("Log//score.txt", "a+")
    file.write(str(score_val))
    file.write("\n")
    file.close()


# bg
def bg():
    global background
    global state, game_over, pos,b_show
    background = pygame.image.load('Icons//background.png')
    mixer.music.stop()
    mixer.music.load("Audio//background.wav")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)
    state = True
    game_over = False



# Game Over
game_over = False
f = False
n = 0
j = 0
end = False


def gameover():
    global background, f, end, file, score_val, show
    mixer.music.stop()
    background = pygame.image.load('Icons//gameover.png')
    if not end:
        txt = score_font.render('Press ENTER To Show The Score ', True, (255, 255, 255))
        screen.blit(txt, (205, 550))
    f = True
    show = False


# Score
score_font = pygame.font.Font('freesansbold.ttf', 24)


def score(x, y):
    tx = score_font.render('SCORE : ' + str(score_val), True, (255, 255, 255))
    screen.blit(tx, (x, y))


def re(le, x, y):
    pygame.draw.rect(screen, (0, 0, 0), (2, 40, 300, 25), 4)
    if le >= 0 and le <= 60:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, l, 25))
    elif le >= 60 and le <= 120:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, l, 25))
    elif le >= 120 and le <= 180:
        pygame.draw.rect(screen, (125, 120, 160), (x, y, l, 25))
    elif le >= 180 and le <= 240:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, l, 25))
    elif le >= 240 and le <= 300:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, l, 25))


# DISPLAY
def show_power(x, y):
    p = font.render("POWER : " + str(power), True, (255, 255, 255))
    screen.blit(p, (x, y))


def player(x, y):
    global pos
    screen.blit(playerImg, (x, y))
    pos = ()


def san(x, y):
    screen.blit(simg, (x, y))


def virus(x, y, i):
    screen.blit(virusimg[i], (x, y))


# Fire-Bullet
def fire_bullet(x, y):
    global bullet_state
    if bullet_state == "fire" or power >= 100:
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 20, y + 20))


# Collision Detection
def isCollision(vX, vY, bulletX, bulletY):
    distance = math.sqrt(math.pow(vX - bulletX, 2) + (math.pow(vY - bulletY, 2)))
    if distance < 29:
        if bullet_state == 'fire':
            mixer.Sound('Audio//bullet_hit.wav').play()
        return True
    else:
        return False


def isgameover(xe, ye, xd, yd):
    distance = ((xd - xe) ** 2 + (yd - ye) ** 2) ** 0.5
    if distance < 29:
        return True
    else:
        return False


def power_up(sx, sy, playerX, playerY):
    distance = math.sqrt(math.pow(sx - playerX, 2) + (math.pow(sy - playerY, 2)))
    if distance <= 29:
        return True
    else:
        return False


# PoP-Up Messages
cloud = pygame.image.load('Icons//cloud.png')
turn = False
kill_temp = 50


def cloud_pop(message, turn):
    if turn:
        screen.blit(cloud, (0, 420))
        font_message = pygame.font.Font('freesansbold.ttf', 14)
        if turn == 1:
            p1 = font_message.render(message[0], True, (0, 0, 0))
            p2 = font_message.render(message[1], True, (0, 0, 0))
            p3 = font_message.render(message[2], True, (0, 0, 0))
            p4 = font_message.render(message[3], True, (0, 0, 0))
            screen.blit(p1, (50, 480))
            screen.blit(p2, (35, 495))
            screen.blit(p3, (44, 507))
            screen.blit(p4, (47, 520))


running = True
while running:

    local_time = int(time.process_time())

    if not game_over and state and local_time >= game_time + 1:
        score_val += 1
        game_time = local_time

    screen.blit(background, (0, 0))
    if game_over:
        gameover()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            store()
            show_s = False
            sys.exit()

        # KEY - Events
        if event.type == pygame.KEYDOWN:

            if game_over:
                if event.key == pygame.K_RETURN:
                    n = 2
                    end = True


            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 2
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
                    if power >= 100:
                        mixer.Sound('Audio//bullet_fire.wav').play()
                        if s_i==1:
                            power = power - 100
                            l = l - 60
                        if s_i==2:
                            power = power - 50
                            l = l - 30
                        if s_i==3:
                            power = power - 25
                            l = l - 15
                        if s_i==4:
                            power = power - 10
                            l = l - 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
        if not state:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    show = True
                    st()
                    if show_s:
                        show_b = True
                        shop()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                st()
        if game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:
                    pos = pygame.mouse.get_pos()
                    show = True
                    score_page()

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()

    # Player Movemment
    playerY += playerY_change
    playerX += playerX_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Virus Movement
    if state is True:

        for i in range(virus_count):
            vY[i] += vchange_Y[i]

            if vY[i] <= 0:
                vchange_Y[i] = 0.3
                if vX[i] >= 200:
                    vchange_X[i] = random.randint(100, 350)
                    vX[i] += vchange_X[i]
                else:
                    vX[i] = 600

            elif vY[i] >= 536:
                vchange_Y[i] = -0.3
                if vX[i] <= 700:
                    vchange_X[i] = random.randint(100, 350)
                    vX[i] -= vchange_X[i]
                else:
                    vX[i] = 400
            virus(int(vX[i]), int(vY[i]), i)
            collision = isCollision(vX[i], vY[i], bulletX, bulletY)
            if collision:
                bulletY = 300
                bullet_state = "ready"
                kill_value += 1
                coin += 1
                file_coin.write(str(coin))
                file_coin.flush()
                file_coin.seek(0)
                vX[i] = random.randint(400, 700)
                vY[i] = random.randint(0, 536)
            # Game Over
            col_game = isgameover(vX[i], vY[i], playerX, playerY)
            if col_game:
                for k in range(virus_count):
                    vX[k] = 20000
                    vY[k] = 20000
                    sx = 20000
                    sy = 20000
                    schange_x = schange_y = 0
                    vchange_X[k] = vchange_Y[k] = 0
                sh_y = 2000
                sc_y = 2000
                po_y = 2000
                game_over = True

            if not game_over:
                virus(int(vX[i]), int(vY[i]), i)

    # Bullet movement
    if bulletX >= 736:
        bulletX = playerX
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change

    # PowerUp movement
    sy += schange_y
    if sy <= 0:
        schange_y = 0.3
        if sx >= 200:
            schange_x = random.randint(100, 350)
            sx += schange_x
        else:
            sx = 600
    if sx == 0:
        sx = 10
    elif sy >= 536:
        schange_y = -0.3
        if sx <= 700:
            schange_x = random.randint(100, 350)
            sx -= schange_x
        else:
            sx = 400

    collision = power_up(sx, sy, playerX, playerY)
    if collision:
        if power >= 0 and power <= 500:
            power += 5
            l += 3
    if power > 500:
        extra_power = power - 500
        power = power - extra_power
    if l > 300:
        extra_l = l - 300
        l = l - extra_l
    if not game_over and state is True:
        score(sc_x, sc_y)
        re(l, po_x, po_y)
        san(int(sx), int(sy))
        player(playerX, playerY)
        show_power(sh_x, sh_y)
    if state is False or g_show is True:
        st()
    if game_over: 
        gameover()
    if f and n == 2:
        score_page()
    if b_show:
        ballon(y_pos)

        y_pos -= y_ch
        y_ch += 1
        if y_pos == 0:
            b_show = False
    if show_s:
        shop()

    # PoP Up Guy
    if score_val < 2:
        cloud_pop(['Saddle Up !! ', 'Maintain Social', 'Distance and', 'Survie Long'], turn)

    # Kill Count Pop-Up
    if kill_value >= kill_temp:
        turn = 1
        cloud_pop(['Guess What ', 'You Are Slaying', 'You\'ve Killed', str(kill_value) + ' Particles'], turn)
        if kill_value == kill_temp + 1:
            kill_temp += 50

    # Min Survival Pop-Up
    if score_val % 60 in [0, 1, 2, 3] and score_val > 4:
        turn = 1
        rough = score_val // 60
        cloud_pop(['Well Actually ', 'You Have Survived', 'For More Than', str(rough) + ' Minutes'], turn)

    pygame.display.update()
