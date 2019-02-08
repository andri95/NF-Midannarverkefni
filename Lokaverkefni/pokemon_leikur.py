#Lokaverkefni - Andri Fannar Pétursson

import pygame
import random


#Innbyggður 'base' klasi fyrir sýnilega objecta í pygame.
#Notaði fyrst bara imageload sem kall, en þurfti sprite klasann fyrir rect collision eiginleikann.
class Leikmadur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Notandi.__init__(self)


pygame.init() #Setur allar pygame modules í gang

hvitur = (255, 255, 255) #Bý til breytu sem ég nota sem bakgrunnslit.
pygame.display.set_caption("Gotta catch em´all!") #Skilaboðin sem birtast efst á glugganum.
yfirbord = pygame.display.set_mode((640, 480)) #Bý til breytuna yfirborð, sem inniheldur gluggann sem leikurinn birtist á.
yfirbord.fill(hvitur) #Nota yfirborðsbreytuna og fylli bakgrunninn með hvitur breytunni.

x_stada = 0 #Set hérna x og y byrjunarstöðuna fyrir leikmanninn.
y_stada = 220

leik_madur = pygame.sprite.Sprite() #Hérna nota ég Sprite klasann og bý til úr honum leikmann
leik_madur.rect = pygame.Rect(x_stada, y_stada, 50, 50) #Nota rect eiginleika Sprite til að vita staðsetningu leikmannsins. x_stada og y_stada = núverandi staðsetning. 50/50 = stærð
leik_madur.mynd = pygame.image.load('ash.png').convert() #Hérna loada ég inn mynd sem eiginleika leikmannsins

kula_1 = pygame.sprite.Sprite() #Geri það sama fyrir allar kúlurnar til að fá Rect eiginleikann.
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

pikachu = pygame.image.load('picachu.png').convert() #Hef pikachu bara sem mynd þar sem ég þarf ekki á Rect eiginleikanum að halda í þessum leik.


pygame.font.init() #Hérna nota ég innbyggt font function til að gera skrifað texta á skjáinn.
letur = pygame.font.SysFont('Monospace', 15) #Set leturgerð og leturstærð.

keyrir = True #Byrjunargildið á keyrir er True, nota þessa breytu til að láta forritið vita hvort það eigi að keyra.
klukka = pygame.time.Clock() #Eins og ég skil þetta ákvarðar þetta hversu oft á sekúndu skjárinn refreshar sig.
klukka_ticrate = 60 #Skjárinn uppfærist 60x á sekúndu.


while keyrir: #Á meðan breytan keyrir = True.
    for event in pygame.event.get(): #Í hvert skipti sem ýtt er á takka keyrist þessi for lykkja.
        if event.type == pygame.QUIT: #Ef glugganum er lokað hættir leikurinn að keyra (keyrir verður False).
            keyrir = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Ef ýtt er á ESC takkann hættir leikurinn að keyra.
            keyrir = False


        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: #Hérna nota ég Rect eiginleikann til að segja kallinum að hreyfast um 10px þegar ýtt er á ákveðna takka.
            leik_madur.rect.y -= 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            leik_madur.rect.y += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            leik_madur.rect.x += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            leik_madur.rect.x -= 10

        texti = letur.render('Finndu Pokémon kúluna sem inniheldur Pikachu!', False, (0,0,0)) #Nota render eiginleika font til að teikna textann á skjáinn.

        if pygame.sprite.collide_rect(leik_madur, kula_1): #Í eftirfarandi skilyrðissetningum nota ég Rect eiginleikann til að detecta Collision milli leikmanns og kúlu.
            texti_sigur = letur.render('Þú fannst Pikachu!!', False, (0,0,0))
            yfirbord.blit(texti_sigur, (300, 200)) #Hérna 'blittar'/teiknar forritið textann á yfirborð(skjárinn) á ákveðna staðsetningu.
            yfirbord.blit(pikachu, (275, 300))
        elif pygame.sprite.collide_rect(leik_madur, kula_2):
            texti_tap = letur.render('Þessi Pokémon kúla er tóm!', False, (0,0,0))
            yfirbord.blit(texti_tap, (300,200))
        elif pygame.sprite.collide_rect(leik_madur, kula_3):
            texti_tap = letur.render('Þessi Pokémon kúla er tóm!', False, (0, 0, 0))
            yfirbord.blit(texti_tap, (300, 200))
        elif pygame.sprite.collide_rect(leik_madur, kula_4):
            texti_tap = letur.render('Þessi Pokémon kúla er tóm!', False, (0, 0, 0))
            yfirbord.blit(texti_tap, (300, 200))

        yfirbord.blit(texti, (25, 25)) #Hérna 'teiknar' forritið breytuna texti á yfirborðið á ákveðna staðsetningu,
        yfirbord.blit(leik_madur.mynd, leik_madur.rect.topleft) #Hérna 'teiknar' forritið .mynd eiginleika leikmanns objectsins. Punkturinn sem Rect notar settur í topleft hornið.
        yfirbord.blit(kula_1.mynd, kula_1.rect.topleft) #Geri það sama hér fyrir allar kúlurnar.
        yfirbord.blit(kula_2.mynd, kula_2.rect.topleft)
        yfirbord.blit(kula_3.mynd, kula_3.rect.topleft)
        yfirbord.blit(kula_4.mynd, kula_4.rect.topleft)

        pygame.display.flip() #Notaði þetta í staðinn fyrir display update sem virkaði ekki hjá mér. En þetta gerir það sama held ég.
        yfirbord.fill(hvitur) #Set þetta aftur hérna til að koma í veg fyrir að Sprite-inn skilji slóð á eftir sig.