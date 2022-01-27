import pygame
from random import randint

w, h = 864, 554
act = 'Stand'
go = ''
num = 7
speed = 60
spsh = 0
numsp = 0
vecUP = 0
scht = 0
sdvig = False
stand = True
kUp = True
flip = False

rects = open('old/rect.txt').read().replace('\n', ' ').split()

pygame.init()
window = pygame.display.set_mode((w, h))
pygame.display.set_caption("Miku jump v1")
font = pygame.font.SysFont('cambriacambriamath', 32)
clock = pygame.time.Clock()
fon = pygame.image.load('pic/fon.jpg')
plat = pygame.image.load('pic/plat2.png')
plat.set_colorkey((255, 255, 255))

Miku = pygame.sprite.Sprite()
Miku.image = pygame.image.load('res/Stand0.png')
Miku.rect = Miku.image.get_rect()
Miku.rect.width, Miku.rect.height = 30, 64
Miku.rect.x, Miku.rect.y = 220, 350

group = pygame.sprite.Group()

plat = pygame.sprite.Sprite()
plat.image = pygame.image.load('pic/plat2.png')
plat.image.set_colorkey((255, 255, 255))
plat.rect = plat.image.get_rect()
plat.rect.x, plat.rect.y = 200, 400
group.add(plat)

play = True
while play:
    clock.tick(speed)
    spsh = spsh + 1 if spsh < speed else 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                go, flip = 'RIGHT', False
            if event.key == pygame.K_LEFT:
                go, flip = 'LEFT', True

            if not stand:
                continue
            kUp = False
            numsp = 0
            if event.key == pygame.K_UP:
                act, num, vecUP = 'jump', 8, 18
            if event.key == pygame.K_a:
                act, num = 'attack', 7
            if event.key == pygame.K_l:
                act, num = 'loss', 2
            if event.key == pygame.K_w:
                act, num = 'win', 11

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                go = ''
            kUp = True

    if go == 'RIGHT' and not flip:
        Miku.rect.x = Miku.rect.x + 5 if Miku.rect.x < w-Miku.rect.width else Miku.rect.x
    elif go == 'LEFT':
        Miku.rect.x = Miku.rect.x - 5 if Miku.rect.x > 0 else Miku.rect.x

    Miku.rect.y -= vecUP
    vecUP = vecUP - 1 if not stand and vecUP > -15 else vecUP

    if kUp and (numsp == num-1 or act == 'go'):
        act, num = 'Stand', 19

    if go and stand:
        act, num = 'go', 7

    if not stand:
        act, num = 'jump', 8

    if spsh % 5 == 0:
        numsp += 1
        if act == 'jump' and not stand and numsp == 7:
            numsp -= 1
    numsp = 0 if numsp >= num else numsp

    stand = False
    if pygame.sprite.spritecollide(Miku, group, False):
        for Plat in group:
            if Miku.rect.colliderect(Plat):
                if abs(Miku.rect.x + Miku.rect.width - Plat.rect.x) < 6:
                    Miku.rect.x = Plat.rect.x - Miku.rect.width
                if abs(Plat.rect.x + Plat.rect.width - Miku.rect.x) < 6:
                    Miku.rect.x = Plat.rect.x + Plat.rect.width
                if abs(Miku.rect.y + Miku.rect.height - Plat.rect.y) < 16:
                    stand = True
                    Miku.rect.y = Plat.rect.y - Miku.rect.height + 5
                    vecUP = 0
                    if list(group).index(Plat) == len(group)-1:
                        plat = pygame.sprite.Sprite()
                        plat.image = pygame.image.load('pic/plat2.png')
                        plat.image.set_colorkey((255, 255, 255))
                        plat.rect = plat.image.get_rect()
                        plat.rect.x, plat.rect.y = Plat.rect.x+randint(130, 200)+spsh, Plat.rect.y+randint(-100, 50)
                        group.add(plat)
                        scht += 1
                        sdvig = True

                # if abs(Plat.rect.y + Plat.rect.height - Miku.rect.y) < 20:
                #     vecUP = -1

    if Miku.rect.y > 500:
        font = pygame.font.SysFont('cambriacambriamath', 32)
        window.blit(fon, (0, 0))
        text = font.render('Счёт: ' + str(scht), True, (100, 100, 250))
        window.blit(text, (0, 0))
        font = pygame.font.SysFont('cambriacambriamath', 85)
        text = font.render('Ты проиграл', True, (30, 30, 150))
        window.blit(text, (w // 4-50, h // 2-80))
        pygame.display.flip()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

    for Plat in group:
        if Plat.rect.x < -100:
            Plat.kill()

    # print(vecUP)
    window.blit(fon, (0, 0))
    Miku.image = pygame.image.load('res/' + act + str(numsp) + '.png')
    Miku.image = pygame.transform.flip(Miku.image, flip, False)
    Miku.image.set_colorkey((150, 200, 250))

    xst, yst = int(rects[rects.index(act)+1]), int(rects[rects.index(act)+2])-3,
    if flip:
        xst = 0

    if sdvig and not act == 'jump':
        sdx, sdy = 0, 0
        k = 7
        if w // 3 - Miku.rect.x > k:
            sdx = k
        elif w // 3 - Miku.rect.x < -k:
            sdx = -k
        if h // 2 - Miku.rect.y > k:
            sdy = k
        elif h // 2 - Miku.rect.y < -k:
            sdy = -k

        Miku.rect.x += sdx
        Miku.rect.y += sdy
        for Plat in group:
            Plat.rect.x += sdx
            Plat.rect.y += sdy

        if sdx == sdy == 0:
            sdvig = False

    for Plat in group:
        window.blit(Plat.image, (Plat.rect.x, Plat.rect.y-10))
        # pygame.draw.rect(window, (255, 0, 0), (Plat.rect.x, Plat.rect.y, Plat.rect.width, Plat.rect.height), 2)
    window.blit(Miku.image, (Miku.rect.x-xst, Miku.rect.y-yst))

    text = font.render('Счёт: ' + str(scht), True, (100, 100, 250))
    window.blit(text, (0, 0))

    # pygame.draw.rect(window, (255, 0, 0), (Miku.rect.x, Miku.rect.y, Miku.rect.width, Miku.rect.height), 2)

    pygame.display.flip()
