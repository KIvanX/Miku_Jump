
import os
import time
import pygame

pygame.init()
window = pygame.display.set_mode((800, 500))

file = open('rect.txt', 'w')
for path in os.listdir('../res'):
    if path[len(path)-5] != '0':
        continue
    image = pygame.image.load('../res/'+path)
    path = path[0:-5]
    image = pygame.transform.scale(image, (image.get_width()*8, image.get_height()*8))
    window.fill('#000000')
    window.blit(image, (0, 0))
    pygame.display.flip()
    wait = True
    x, y = 0, 0
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file.close()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    x, y = x//8, y//8
                    file.write(path+' '+str(x)+' '+str(y)+'\n')
                wait = False

    time.sleep(1)
    print(path, x, y)

file.close()
