from pygame import *    #import the pygame with *
import menu             #importing code from menu
import random           #importing random, so we can do what we want to do using random

from classes import *




def run_game():         #to define run_game, so the code can be call when using "run_game" code
    """game play interface"""
    screen = pygame.display.set_mode((800, 600))        #size of the game's window display
    pygame.display.set_caption("Jet mission")                  #to set the name of the game


    scores = 0              #to set the score on the game
    theClock = pygame.time.Clock()      #to track the time
    bg_image = Star_bg("star.gif")      #to put the background of the game

    #coordinate of moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init()


    #creating a jet
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 40
    asteroid_timer = pygame.time.get_ticks()    #to set the time for asteroid_timer
    while True:                            #loop so it can run it agian
        theClock.tick(Fps)              #to sets the game's speed to run
        Fps += 0.01             #game phase goes faster after every frame

        """background move"""

        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width:
            x = 0
        if x1 < 0:                  #spawning the asteroid
            x1 = bg_image.width

        # create score board

        font=pygame.font.SysFont("Times New Romans",36)         #the size and type of the font
        score_board=font.render("score:"+str(scores),True,(255,255,255))      #to input the color for the "score" and "score:"

        # update refered to the word's method

        screen.blit(score_board,(10,550))    #put where the score will show       #



        Jet_sprites.draw(screen)        #to input the jet to inside the game

        bullets.draw(screen)            #to input the bullet to inside the game

        asteroid_group.draw(screen)     #to input the asteroid to inside the game
        display.update()                   #update jet and screen view

        event.get()                 #to summon and get the event from others files
        """moving the jet according to key pressed"""

        key = pygame.key.get_pressed()         #to make the key for playing the game
        if key[K_LEFT] and jet1.rect.x>0:      #make the jet go to the left side by pressing the left key and will not disappear when going to the over left
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:   #make the jet go to the right side by pressing the right key and will not disappear when going to the over right
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:    #make the jet go to the down side by pressing the down key and will not disappear when going to the over down
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:     #make the jet go to the up side by pressing the up key and will not disappear when going to the over up
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):   #press space key to call the bullet and and the total of the bullets are not bigger than the jet1 firerate
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42)
            bullets.add(bullet)                  #to add the place for bullets spawn
            pygame.mixer.music.load("LaserBlast.wav")      #to make a sound everytime the bullet spawn
            pygame.mixer.music.play()       #to run and play the sound

        if key[K_ESCAPE]:                   #to make the game back to the fist show which is the menu when pressing escape key
            menu.menu_screen(Button,run_game)

        if key[K_p]:                        #to stop the the game for a while by pressing p key
            menu.pause_menu(Button,run_game)


        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200: #asteroid timer is bigger than 200 or equal with 200
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            asteroid_group.add(asteroid)           #add the asteroid to the asteroid group
            asteroid_timer = pygame.time.get_ticks()    #get the time in pygame.time.get_ticks() for asteroid_timer

        """update the movement of asteroid"""
        for asteroid in asteroid_group:     #looping asteroid in the asteroid_group
            asteroid.movement()     #thw movement of the asteroid
            if asteroid.rect.right <= 0:        #the asteroid disappear when arrive the left screen
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores)  #when the asteroid touch the jet the game will end and show the lose menu and shoing the score that you get

        """update bullet movement on screen"""
        for bullet in bullets: #looping the bullet in bullets
            bullet.movement()
            if bullet.rect.left > 800:     #the bullet will disappear if the bullet reach the right side of the screen
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100   #when everytime the bullet touch the asteroid, the score will increase 100

menu.menu_screen(Button,run_game)       #call to run the game

#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------
"""Acknowledgement:
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""
