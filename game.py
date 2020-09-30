import sys, pygame, random
from pygame.locals import *
pygame.init()

def game(speed): 
    # initializing graphics and colors
    backgroundColor = 0, 0, 0
    size = x, y = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space invaders... IMPROVED') 
    fontwinlose = pygame.font.Font('freesansbold.ttf', 50) 
    fontspace = pygame.font.Font('freesansbold.ttf', 20)   
    fontscore = pygame.font.Font('freesansbold.ttf', 15)

    dinosaurColor = 73, 153, 0
    bulletColor = dinosaurColor
    meteorColor = 255, 153, 51
    explodemeteorcolor = 255, 30, 30
    grey = 192, 192, 192

    # initializing variables
    # Dinosaur
    dinosaurPositionX = 300
    dinosaurPositionY = 350
    # Meteors
    XList = [300]
    YList = [100]
    radiusList = [15]
    sendMeteor = False
    # Bullet
    bulletPositionX = 0
    bulletPositionY = 350
    sendBullet = False
    # Score
    winscore = 0
    losescore = 0

    while winscore < 3 and losescore <= 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]: dinosaurPositionX = dinosaurPositionX - 3
        if pressed[K_RIGHT]: dinosaurPositionX = dinosaurPositionX + 3
        if pressed[K_SPACE]: 
            sendBullet = True
            bulletPositionX = dinosaurPositionX
            bulletPositionY = 350
            dinosaurColor = 73, 153, 0
        pygame.display.update()
        screen.fill(backgroundColor)

        #dinosaur
        pygame.draw.rect(screen, dinosaurColor , (dinosaurPositionX-10, dinosaurPositionY-20, 20, 40))

        # bullet
        if(sendBullet):
            bulletPositionY = bulletPositionY - 5
            k = 0
            while k < len(XList) :
                if (bulletPositionX < XList[k] + radiusList[k] and bulletPositionX > XList[k] - radiusList[k] and bulletPositionY < YList[k] + radiusList[k] and bulletPositionY > YList[k] - radiusList[k]): 
                    pygame.draw.circle(screen, explodemeteorcolor, (XList[k], YList[k]), radiusList[k], 0)
                    del XList[k]
                    del YList[k]
                    del radiusList[k]
                    winscore = winscore + 1
                k = k+1
            pygame.draw.line(screen, bulletColor, (bulletPositionX,bulletPositionY),(bulletPositionX, bulletPositionY-5), 5)
            if bulletPositionY == 50:
                sendBullet = False
                bulletPositionY = 350 #after first bullet has finished a new one can be sent
            
        # meteors 
        # increases y positions for all meteors each turn
        i = 0
        while i < len(YList) :
            YList[i] = YList[i] + 1
            if YList[i] > 490: #if on the floor, disappears
                del XList[i]
                del YList[i]
                del radiusList[i]
                losescore = losescore + 1
            i = i + 1
        # meteors appear w. random X and radius if sendMeteor = True
        if(YList == [] or YList[len(YList)-1] == speed): sendMeteor = True # a new meteor is added
        if sendMeteor:
            XList.append(random.randint(50,550))
            YList.append(100)
            radiusList.append(random.randint(5,20))
            sendMeteor = False
        # draws the meteors 
        j = 0
        while j < len(XList) :
            pygame.draw.circle(screen, meteorColor, (XList[j], YList[j]), radiusList[j], 0)
            j = j+1
         
        #Dinosaur hurt
        s = 0
        while s < len(XList) :
            if (dinosaurPositionX < XList[s] + radiusList[s] and dinosaurPositionX > XList[s] - radiusList[s] and dinosaurPositionY < YList[s] + radiusList[s] and dinosaurPositionY > YList[s] - radiusList[s]): 
                pygame.draw.circle(screen, explodemeteorcolor, (XList[s], YList[s]), radiusList[s], 0)
                del XList[s]
                del YList[s]
                del radiusList[s]
                losescore = losescore +2
                dinosaurColor = explodemeteorcolor
            s=s+1

        #draws scores
        text3 = fontscore.render(str(winscore), 1, (73, 153, 0))
        screen.blit(text3, (80, 320))
        text4 = fontscore.render(str(losescore), 1, explodemeteorcolor)
        screen.blit(text4, (500, 320))

    if losescore >= 5:
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            pygame.display.update()
            screen.fill(backgroundColor)

            text1 = fontwinlose.render('GAME OVER', True, explodemeteorcolor) 
            screen.blit(text1, (140, 150))
            text2 = fontspace.render('Type Space to play again', True, grey) 
            screen.blit(text2, (190, 300))
            pressed = pygame.key.get_pressed()
            if pressed[K_SPACE]: game(speed)

    if winscore >= 3:
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            pygame.display.update()
            screen.fill(backgroundColor)

            text1 = fontwinlose.render('YOU WON', True, dinosaurColor) 
            screen.blit(text1, (170, 150))
            text2 = fontspace.render('Type Space to play again', True, grey) 
            screen.blit(text2, (190, 280))
            pressed = pygame.key.get_pressed()
            if pressed[K_SPACE]: game(speed-20)

#kör spelet
game(200)