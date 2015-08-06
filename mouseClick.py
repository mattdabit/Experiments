#Get Keypresses
# import run
def mouseClick(pygame, num):
    player_times = []
    count = 0 
    while count < num:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_times.append(pygame.time.get_ticks())
                count +=1
    return player_times