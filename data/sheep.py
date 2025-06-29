import random
import pygame

class Sheep:

    def __init__(self):
        self.texture = pygame.transform.scale(pygame.image.load(f'assets/sheep.png'), (64, 64))
        self.hitbox = pygame.Rect(0, 0, 64, 64)
        self.x = random.randint(0, 24*32)
        self.y = random.randint(0, 18*32)
        self.adrenalin = [0, [0, 0]]
        self.last_pos = [self.x, self.y]

    def Draw(self, screen):  
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox)
        screen.blit(self.texture, (self.x, self.y))

    def Controll(self,screen,difficult):
        if self.adrenalin[0] > 0: self.adrenalin[0]-=1

        if self.adrenalin[0] == 0 or self.x < 0 or self.y < 0 or self.x > 24*32 or self.y > 18*32:
            self.adrenalin[0] = random.randint(2, 10) * 120
            self.adrenalin[1][0] = random.randint(-1, 1)
            self.adrenalin[1][1] = random.randint(-1, 1)

        self.x += self.adrenalin[1][0]*difficult
        self.y += self.adrenalin[1][1]*difficult

        self.last_pos = [self.x, self.y]

        self.Draw(screen)