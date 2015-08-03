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
session =[]
ran_session = [0, 1]
pygame.init()
pygame.mixer.init()
size = (1900, 1080)
white = (255, 255, 255)
trials = 20
trial_type = []
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drummer Experiment")
pygame.display.toggle_fullscreen()

def run():
    global trial
    global player_times
    global session
    global trial_type
    first = random.choice(ran_session)
    if first == 0:
        session = ['0']
        trial_type = ['350ms', '550ms']
        textCreate(pygame,screen,"We will start with a pace of 350ms! Remember to continue the pace", white)
        pygame.time.delay(5000)
        clearScreen(screen)
    else:
        session =  ['1']
        trial_type = ['550ms', '350ms']
        textCreate(pygame,screen,"We will start with a pace of 550ms! Remember to continue the pace", white)
        pygame.time.delay(5000)
        clearScreen(screen)

    while trial != trials:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
   

        #Run a trial
        textCreate(pygame, screen,"X", white)
        pygame.time.delay(1000)

        if trial < 10 and first == 0:
            playAudio(pygame, 0)
            sess
        elif trial < 10 and first == 1:
            playAudio(pygame, 1)
        elif trial >= 10 and first == 1:
            playAudio(pygame, 0)
        elif trial >= 10 and first == 0:
            playAudio(pygame, 1)
        play_time = mouseClick(pygame, 25)
        playTone(16000, 500,2)

        #Consolidate data
        for i in play_time:
            player_times.append(i)

        #Feedback calculation
        r = rate(play_time)
        rr = round_rate(play_time)

        std_now = stdev(r[2:])
        mean_now = mean(r[2:])

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
            pygame.time.delay(4000)
            textCreate(pygame, screen,"You are done! Thank you!", white)
        elif trial == 10 and first == 0:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(4000)
            textCreate(pygame, screen, "The pace will now change to 550ms", white)
            pygame.time.delay(2000)
            textCreate(pygame, screen,"Trial complete. Prepare for next trial.", white)
        elif trial == 10 and first == 1:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(4000)
            textCreate(pygame, screen, "The pace will now change to 350ms", white)
            pygame.time.delay(2000)
            textCreate(pygame, screen,"Trial complete. Prepare for next trial.", white)
        else:
            textCreate(pygame, screen, "Your average pace: %s, Your standard deviation: %s" %(mean_now, int(std_now)), white)
            pygame.time.delay(4000)
            textCreate(pygame, screen,"Trial complete. Prepare for next trial.", white)
        pygame.time.delay(3000)        

if __name__ == '__main__':
    train(pygame, screen)
    run()
    createFile(name, session, trial_type, player_times, std, m, r_std, r_m)

# Mouse response rate 
    # 500hz - 2ms
# plot covariance Fn
# if person speeds over time shows + corr need to detrend data
# Wing analysis 