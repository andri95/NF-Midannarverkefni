#Lokaverkefni - Andri Fannar Pétursson

import pygame
import random
import socket
import threading



pygame.init()

hvitur = (255, 255, 255)
pygame.display.set_caption("Gotta catch em´all!")
yfirbord = pygame.display.set_mode((640, 480))
yfirbord.fill(hvitur)

def createThread(target):
    thread = threading.Thread(target = target)
    thread.daemon = True
    thread.start()

host = '127.0.0.1'
port = 60000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def recieveData():
    while True:
        data = sock.recv(1024).decode()
        data = data.split('-')
        leik_madur.rect.x = int(data[0])
        leik_madur.rect.y = int(data[1])
        print(data)


createThread(recieveData)

class Leikmadur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Notandi.__init__(self)

x_stada = 0
y_stada = 175

x_stada2 = 0
y_stada2 = 275

leik_madur = pygame.sprite.Sprite()
leik_madur.rect = pygame.Rect(x_stada, y_stada, 50, 50)
leik_madur.mynd = pygame.image.load('ash.png').convert()

leik_madur2 = pygame.sprite.Sprite()
leik_madur2.rect = pygame.Rect(x_stada2, y_stada2, 50, 50)
leik_madur2.mynd = pygame.image.load('ash2.png').convert()

kula_1 = pygame.sprite.Sprite()
kula_1.rect = pygame.Rect(200, 300, 50, 50)
kula_1.mynd = pygame.image.load('pokemon_kula.png').convert()

kula_2 = pygame.sprite.Sprite()
kula_2.rect = pygame.Rect(200, 100, 50, 50)
kula_2.mynd = pygame.image.load('pokemon_kula.png').convert()

kula_3 = pygame.sprite.Sprite()
kula_3.rect = pygame.Rect(580, 100, 50, 50)
kula_3.mynd = pygame.image.load('pokemon_kula.png').convert()

kula_4 = pygame.sprite.Sprite()
kula_4.rect = pygame.Rect(580, 300, 50, 50)
kula_4.mynd = pygame.image.load('pokemon_kula.png').convert()

pikachu = pygame.image.load('picachu.png').convert()


pygame.font.init()
letur = pygame.font.SysFont('Monospace', 25)

keyrir = True
klukka = pygame.time.Clock()
klukka_ticrate = 60
stadsetning = 3


while keyrir:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keyrir = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            keyrir = False

        xStada = leik_madur2.rect.x
        yStada = leik_madur2.rect.y
        print(xStada, yStada)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            leik_madur2.rect.y -= 10
            send_data = '{}-{}'.format(xStada, yStada).encode()
            sock.send(send_data)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            leik_madur2.rect.y += 10
            send_data = '{}-{}'.format(xStada, yStada).encode()
            sock.send(send_data)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            leik_madur2.rect.x += 10
            send_data = '{}-{}'.format(xStada, yStada).encode()
            sock.send(send_data)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            leik_madur2.rect.x -= 10
            send_data = '{}-{}'.format(xStada, yStada).encode()
            sock.send(send_data)

        texti = letur.render('Finndu Pokémon kúluna sem inniheldur Pikachu!', False, (0,0,0))

        texti_sigur = letur.render('Þú fannst Pikachu!!', False, (0, 0, 0))
        texti_osigur = letur.render('Leikmaður1 fann Pikachu :(', False, (0, 0, 0))
        texti_tap = letur.render('Þessi Pokémon kúla er tóm!', False, (0, 0, 0))

        #Ef leikmadur2 vinnur:
        if pygame.sprite.collide_rect(leik_madur2, kula_1):
            if stadsetning == 1:
                yfirbord.blit(texti_sigur, (300, 200))
                yfirbord.blit(pikachu, (275, 300))
            else:
                yfirbord.blit(texti_tap, (300, 200))
        elif pygame.sprite.collide_rect(leik_madur2, kula_2):
            if stadsetning == 2:
                yfirbord.blit(texti_sigur, (300, 200))
                yfirbord.blit(pikachu, (275, 100))
            else:
                yfirbord.blit(texti_tap, (300,200))
        elif pygame.sprite.collide_rect(leik_madur2, kula_3):
            if stadsetning == 3:
                yfirbord.blit(texti_sigur, (300, 200))
                yfirbord.blit(pikachu, (515, 100))
            else:
                yfirbord.blit(texti_tap, (300, 200))
        elif pygame.sprite.collide_rect(leik_madur2, kula_4):
            if stadsetning == 4:
                yfirbord.blit(texti_sigur, (300, 200))
                yfirbord.blit(pikachu, (515, 300))
            else:
                yfirbord.blit(texti_tap, (300, 200))

        #Ef leikmadur1 vinnur:
        if pygame.sprite.collide_rect(leik_madur, kula_1):
            if stadsetning == 1:
                yfirbord.blit(texti_osigur, (300, 200))
                yfirbord.blit(pikachu, (275, 300))

        elif pygame.sprite.collide_rect(leik_madur, kula_2):
            if stadsetning == 2:
                yfirbord.blit(texti_osigur, (300, 200))
                yfirbord.blit(pikachu, (275, 100))

        elif pygame.sprite.collide_rect(leik_madur, kula_3):
            if stadsetning == 3:
                yfirbord.blit(texti_osigur, (300, 200))
                yfirbord.blit(pikachu, (515, 100))

        elif pygame.sprite.collide_rect(leik_madur, kula_4):
            if stadsetning == 4:
                yfirbord.blit(texti_osigur, (300, 200))
                yfirbord.blit(pikachu, (515, 300))

        yfirbord.blit(texti, (25, 25))
        yfirbord.blit(leik_madur.mynd, leik_madur.rect.topleft)
        yfirbord.blit(leik_madur2.mynd, leik_madur2.rect.topleft)
        yfirbord.blit(kula_1.mynd, kula_1.rect.topleft)
        yfirbord.blit(kula_2.mynd, kula_2.rect.topleft)
        yfirbord.blit(kula_3.mynd, kula_3.rect.topleft)
        yfirbord.blit(kula_4.mynd, kula_4.rect.topleft)

        pygame.display.flip()
        yfirbord.fill(hvitur)