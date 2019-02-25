import pygame
import random

class Character(object):
    def __init__(self):
        self.x_dir = 25
        self.y_dir = 25
        self.character_height = 32
        self.character_width = 32

class Hero(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = 250
        self.y = 250

    def move_hero(self, event):
        if event.key == 273:
            self.y -= self.y_dir
        elif event.key == 274:
            self.y += self.y_dir
        elif event.key == 276:
            self.x -= self.x_dir
        elif event.key == 275:
            self.x += self.x_dir

    def display(self, screen):
        hero_img = pygame.image.load("images/hero.png").convert_alpha()
        screen.blit(hero_img, (self.x, self.y))

    def screen_stay(self, width, height):
        # RIGHT: character goes past right side of display:
        if self.x + self.character_width > width:
            self.x = width - self.character_width
        # BOTTOM: character goes above bottom of display:
        if self.y + self.character_height > height:
            self.y = height - self.character_height
        # LEFT: character goes past left side of display:
        if self.x < 0:
            self.x = 0
        # TOP: character goes past the top of display:
        if self.y < 0:
            self.y = 0

class Monster(Character):
    def __init__(self):
        Character.__init__(self)
        self.x = 50
        self.y = 100
        self.x_dir = 0
        self.y_dir = 1

    def display(self, screen):
        monster = pygame.image.load("images/monster.png").convert_alpha()
        screen.blit(monster, (self.x, self.y))

    def screen_loop(self, width, height):
        # RIGHT: character goes past right side of display:
        if self.x + self.character_width > width:
            self.x = 0
        # BOTTOM: character goes above bottom of display:
        if self.y + self.character_height > height:
            self.y = 0
        # LEFT: character goes past left side of display:
        if self.x < 0:
            self.x = width - self.character_width
        # TOP: character goes past the top of display:
        if self.y < 0:
            self.y = height - self.character_height

    def change_direction(self):
        direction = random.randint(1, 8)
        if direction == 1:
            #Move north
            self.x_dir = 0
            self.y_dir = -2
        if direction == 2:
            #Move east
            self.y_dir = 0
            self.x_dir = 2
        if direction == 3:
            #Move south
            self.x_dir = 0
            self.y_dir = 2
        if direction == 4:
            #Move west
            self.y_dir = 0
            self.x_dir = -2
        if direction == 5:
            #Move southwest
            self.y_dir = 2
            self.x_dir = -2
        if direction == 6:
            #Move northwest
            self.y_dir = -2
            self.x_dir = -2
        if direction == 7:
            #Move northeast
            self.y_dir = -2
            self.x_dir = 2
        if direction == 8:
            #Move southeast
            self.y_dir = 2
            self.x_dir = 2

    def movement(self):
        self.x += self.x_dir
        self.y += self.y_dir


def main():
    width = 510
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    monster = Monster()
    hero = Hero()
    stop_game = False
    counter = 0

    while not stop_game:
        counter += 1
        if counter >= 120:
            monster.change_direction()
            counter = 0

        for event in pygame.event.get():
            # Event handling

            if event.type == pygame.KEYUP:
                hero.move_hero(event)

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        # Draw background

        # Game display
        bg = pygame.image.load("images/background.png").convert_alpha()
        screen.blit(bg, (0, 0))

        monster.movement()
        monster.display(screen)
        monster.screen_loop(width, height)

        hero.display(screen)
        hero.screen_stay(width, height)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()