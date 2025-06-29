import math
import time
import keyboard
import pygame

from data.player import Player
from data.sheep import Sheep

pygame.init()

background = pygame.image.load(f'assets/background.png')
background = pygame.transform.scale(background, (24*32, 18*32))

difficult = 1

font = pygame.font.SysFont(None, 36)

screen = pygame.display.set_mode((24*32, 18*32))
clock = pygame.time.Clock()

def end():
    pygame.mixer.music.load(f'assets/snd.mp3')
    pygame.mixer.music.play()
    time.sleep(15)
        

def main():
    global difficult
    player = Player()
    sheep = Sheep()

    difficult = round(difficult, 2)

    while True:

        clock.tick(100*difficult)
        screen.blit(background, (0, 0))
        player.Controll(screen)
        sheep.Controll(screen, difficult)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()
        
        screen.blit(font.render(f'Difficult {difficult}', False, (0, 0, 0)), (0, 0))
        screen.blit(font.render(f'[p] - reload', False, (0, 0, 0)), (0, 25))
        screen.blit(font.render(f'Complete 10 score of diffictult to get secret end sound)', False, (0, 0, 0)), (0, 18*32-20))

        if pygame.mouse.get_pressed(5)[0] or keyboard.is_pressed('r'):
            if player.hitbox.colliderect(sheep.hitbox):
                difficult+=0.2
                main()

        pygame.display.flip()

        if keyboard.is_pressed('p'): main()
        if difficult == 10: end()

if __name__ == '__main__':
    main()