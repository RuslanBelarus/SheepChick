import random
import pygame
import keyboard

class Player:

    def __init__(self):
        self.texture = pygame.transform.scale(pygame.image.load(f'assets/player.png'), (64, 64))
        self.x = random.randint(0, 24*32)
        self.y = random.randint(0, 18*32)
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        
    def Draw(self, screen):  
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox)
        screen.blit(self.texture, (self.x, self.y))

    def FirstPersonController(self):
        if keyboard.is_pressed('w'):
            self.y-=1
        if keyboard.is_pressed('s'):
            self.y+=1
        if keyboard.is_pressed('a'):
            self.x-=1
        if keyboard.is_pressed('d'):
            self.x+=1

    def Controll(self, screen):
        self.FirstPersonController()
        self.Draw(screen)