#Text Creator
def textCreate(pygame, screen, text, color):
    size = (1900, 1080)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))
    largeText = pygame.font.Font('freesansbold.ttf',55)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((size[0]/2),(size[1]/2))
    background.blit(TextSurf, TextRect)

    screen.blit(background, (0, 0))
    pygame.display.flip()

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def clearScreen(screen):
    screen.fill((0,0,0))