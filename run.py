#!/usr/bin/python
from playAudio import *
from mouseClick import * 
from textCreator import *
from train import *
from createExcelFile import *
from feedback import *
import sys, pygame

name = input("Subject-->")
trial =  0 
times = [] 

player_times = []
std = []
m = []
r_std = []
r_m =[]
pygame.init()
pygame.mixer.init()
size = (1900, 1080)
white = (255, 255, 255)
trials = 20
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drummer Experiment")
pygame.display.toggle_fullscreen()

def run():
    global trial
    global player_times

    while trial != trials:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
   

        #Run a trial
        textCreate(pygame, screen,"X", white)
        pygame.time.delay(1000)

        if trial <10:
            playAudio(pygame, 0) 
        else:
            playAudio(pygame, 1)
        play_time = mouseClick(pygame, 25)
        playTone(16000, 500,2)

        #Consolidate data
        for i in play_time:
            player_times.append(i)

        #Feedback calculation
        r = rate(play_time)
        rr = round_rate(play_time)

        std_now = stdev(r)
        mean_now = mean(r)

        std.append(std_now)
        m.append(mean_now)

        r_std_now = stdev(rr)
        r_mean_now = mean(rr)

        r_std.append(r_std_now)
        r_m.append(r_mean_now)

        #Next Trial
        clearScreen(screen)
        trial+=1
        if trial == trials:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(3000)
            textCreate(pygame, screen,"You are done! Thank you!", white)
        elif trial == 10:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(3000)
            textCreate(pygame, screen, "The pace will now change to 550ms", white)
            pygame.time.delay(2000)
            textCreate(pygame, screen,"Trial complete. Prepare for next trial.", white)
        else:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(3000)
            textCreate(pygame, screen,"Trial complete. Prepare for next trial.", white)
        pygame.time.delay(3000)        

if __name__ == '__main__':
    train(pygame, screen)
    run()
    createFile(name, ['350ms', '550ms'], player_times, std, m, r_std, r_m)

# Find mouse response rate 
    # 125hz - 8ms
    # 500hz - 2ms
    # 1000hz - 1ms Ideal

# plot covariance Fn
# if person speeds over time shows + corr need to detrend data
# Ivry Keele 1988
# Wing analysis 