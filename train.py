#Instructions
from playAudio import *
from playTone import *
from textCreator import *
from mouseClick import *
from feedback import *
def train(pygame, screen):
    black = (0, 0, 0) 
    white = (255, 255, 255)
    textCreate(pygame,screen,"Hello! In this game you will match the pace by clicking the mouse", white)
    pygame.time.delay(5000)
    clearScreen(screen)

    textCreate(pygame,screen,"An X signals the start of a trial", white)
    pygame.time.delay(4000)
    clearScreen(screen)

    textCreate(pygame,screen,"This tone signals the end of a trial", white)
    playTone(16000, 500,2)
    pygame.time.delay(3000)
    clearScreen(screen)

    textCreate(pygame,screen,"Synchronize with the tone when it begins by clicking the mouse", white)
    pygame.time.delay(5000)
    clearScreen(screen)

    textCreate(pygame,screen,"Continue clicking the mouse at the same pace after the tone stops!", white)
    pygame.time.delay(5000)
    clearScreen(screen)

    textCreate(pygame,screen,"The pace of the tone will either be 350ms or 550ms", white)
    pygame.time.delay(5000)
    clearScreen(screen)


    textCreate(pygame,screen,"Let's practice!", white)
    pygame.time.delay(3000)
    clearScreen(screen)

    textCreate(pygame, screen,"X", white)
    pygame.time.delay(1000)

    playAudio(pygame, 0) 
    play_time = mouseClick(pygame, 25)
    playTone(16000, 500,2)
    r = rate(play_time)
    std_now = stdev(r)
    mean_now = mean(r)
    textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
    pygame.time.delay(3000)

    textCreate(pygame,screen,"Let's practice at 550ms! Make sure to continue the pace!", white)
    pygame.time.delay(5000)
    clearScreen(screen)

    textCreate(pygame, screen,"X", white)
    pygame.time.delay(1000)


    playAudio(pygame, 1) 
    play_time = mouseClick(pygame, 25)
    playTone(16000, 500,2)
    r = rate(play_time)
    std_now = stdev(r)
    mean_now = mean(r)
    textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
    pygame.time.delay(3000)

    textCreate(pygame,screen,"We will start with a pace of 350ms! Remember to continue the pace", white)
    pygame.time.delay(4000)
    clearScreen(screen)

    