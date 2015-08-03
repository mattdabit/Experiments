#PlayAudioFiles
def playAudio(pygame, num):
    if num == 0:
        try:
            sound = pygame.mixer.Sound("350ms.ogg")
            sound.play(loops = 0)
        except pygame.error, message:
            print "cannot load Sound: "+ sound
    elif num ==1:
        try:
            sound = pygame.mixer.Sound("550ms.ogg")
            sound.play(loops = 0)
        except pygame.error, message:
            print "cannot load Sound: "+ sound

    else: 
        print "ERROR: No file with that number"