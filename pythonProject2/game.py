import os

import pygame
import button
from pythonProject2.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("CRUCE")
font=pygame.font.SysFont("arialblack",40)
TEXT_COL = (255,255,255)

doiderosu = pygame.image.load("cartiCruce/2rosu.png").convert_alpha()
doiderosubutton = button.Button(50,500,doiderosu,1)

doidebata = pygame.image.load("cartiCruce/2bata.png").convert_alpha()
doidebatabutton = button.Button(180,500,doidebata,1)

doideghinda = pygame.image.load("cartiCruce/2ghinda.png").convert_alpha()
doideghindabutton = button.Button(310,500,doideghinda,1)

doideverde = pygame.image.load("cartiCruce/2verde.png").convert_alpha()
doideverdebutton = button.Button(440,500,doideverde,1)

treiderosu = pygame.image.load("cartiCruce/3rosu.png").convert_alpha()
treiderosubutton = button.Button(570,500,treiderosu,1)

treidebata = pygame.image.load("cartiCruce/3bata.png").convert_alpha()
treidebatabutton = button.Button(700,500,treidebata,1)

treideghinda = pygame.image.load("cartiCruce/3ghinda.png").convert_alpha()
treideghindabutton = button.Button(830,500,treideghinda,1)

treideverde = pygame.image.load("cartiCruce/3verde.png").convert_alpha()
treideverdebutton = button.Button(960,500,treideverde,1)

patruderosu = pygame.image.load("cartiCruce/4rosu.png").convert_alpha()
patruderosubutton = button.Button(1090,500,patruderosu,1)

patrudebata = pygame.image.load("cartiCruce/4bata.png").convert_alpha()
patrudebatabutton = button.Button(1220,500,patrudebata,1)

patrudeghinda = pygame.image.load("cartiCruce/4ghinda.png").convert_alpha()
patrudeghindabutton = button.Button(1350,500,patrudeghinda,1)

patrudeverde = pygame.image.load("cartiCruce/4verde.png").convert_alpha()
patrudeverdebutton = button.Button(1480,500,patrudeverde,1)

nouaderosu = pygame.image.load("cartiCruce/9rosu.png").convert_alpha()
nouaderosubutton = button.Button(50,330,nouaderosu,1)

nouadebata = pygame.image.load("cartiCruce/9bata.png").convert_alpha()
nouadebatabutton = button.Button(180,330,nouadebata,1)

nouadeghinda = pygame.image.load("cartiCruce/9ghinda.png").convert_alpha()
nouadeghindabutton = button.Button(310,330,nouadeghinda,1)

nouadeverde = pygame.image.load("cartiCruce/9rosu.png").convert_alpha()
nouadeverdebutton = button.Button(440,330,nouadeverde,1)

zecederosu = pygame.image.load("cartiCruce/10rosu.png").convert_alpha()
zecederosubutton = button.Button(570,330,zecederosu,1)

zecedebata = pygame.image.load("cartiCruce/10bata.png").convert_alpha()
zecedebatabutton = button.Button(700,330,zecedebata,1)

zecedeghinda = pygame.image.load("cartiCruce/10ghinda.png").convert_alpha()
zecedeghindabutton = button.Button(830,330,zecedeghinda,1)

zecedeverde = pygame.image.load("cartiCruce/10rosu.png").convert_alpha()
zecedeverdebutton = button.Button(960,330,zecedeverde,1)

asderosu = pygame.image.load("cartiCruce/asrosu.png").convert_alpha()
asderosubutton = button.Button(1090,330,asderosu,1)

asdebata = pygame.image.load("cartiCruce/asbata.png").convert_alpha()
asdebatabutton = button.Button(1220,330,asdebata,1)

asdeghinda = pygame.image.load("cartiCruce/asghinda.png").convert_alpha()
asdeghindabutton = button.Button(1350,330,asdeghinda,1)

asdeverde = pygame.image.load("cartiCruce/asverde.png").convert_alpha()
asdeverdebutton = button.Button(1480,330,asdeverde,1)

def draw_text(text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))

run = True
while run:
    screen.fill((52,78,91))
    doiderosubutton.draw(screen)
    doidebatabutton.draw(screen)
    doideghindabutton.draw(screen)
    doideverdebutton.draw(screen)

    treiderosubutton.draw(screen)
    treidebatabutton.draw(screen)
    treideghindabutton.draw(screen)
    treideverdebutton.draw(screen)

    patruderosubutton.draw(screen)
    patrudebatabutton.draw(screen)
    patrudeghindabutton.draw(screen)
    patrudeverdebutton.draw(screen)

    nouaderosubutton.draw(screen)
    nouadebatabutton.draw(screen)
    nouadeghindabutton.draw(screen)
    nouadeverdebutton.draw(screen)

    zecederosubutton.draw(screen)
    zecedebatabutton.draw(screen)
    zecedeghindabutton.draw(screen)
    zecedeverdebutton.draw(screen)

    asderosubutton.draw(screen)
    asdebatabutton.draw(screen)
    asdeghindabutton.draw(screen)
    asdeverdebutton.draw(screen)
    commands = ["mace4 -c -f cruce.in | interpformat > cruce.out"]
    for arg in commands:
        if os.system(arg) != 0:
            print("Failed to execute command " + arg)
    for event in pygame.event.get(()):
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()