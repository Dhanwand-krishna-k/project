import pygame
from clash import dino
from clash import rockman
from clash import droid

pygame.init()


class Main:
    def __init__(self):
        self.height = 400
        self.width = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load('images/bg.png')
        self.bg1 = pygame.image.load('images/bg1.png')
        self.king = pygame.image.load('images/king.png')
        self.play = pygame.transform.scale(pygame.image.load('images/video.png'), (40, 40))
        self.running = True
        self.elix = 0
        self.char_bg = []
        self.start_char_bg = []
        self.actors = []
        self.index = 0
        self.pos = (0, 0)
        self.pos_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.pre_selected = ''
        # bg picture =0,card cord
        self.gloss = {'dino': (0, 10, 10),
                      'rockman': (1, 10, 110),
                      'droid': (2, 10, 210)
                      }

        for flag in range(1,4):
            self.char_bg.append(
                pygame.transform.scale(pygame.image.load('images/backgrounds/' + str(flag) + '.png'), (80, 80)))

    def home_window(self):
        self.screen.blit(self.bg1, (0, 0))
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(350, 250, 100, 50))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(350, 250, 100, 50), 3)
        self.screen.blit(self.play, (380, 255))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if pygame.mouse.get_pressed()[0] == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 350 and pos[0] <= 450 and pos[1] >= 250 and pos[1] <= 300:
                    break

            pygame.display.update()

    def drawWindow(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.king, (100, 150))
        self.screen.blit(self.king, (600, 150))

    def elixer_bar(self, x, y):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, 10, 380), 2)
        for i in range(1, 11):
            if i <= self.elix:
                pygame.draw.rect(self.screen, (200, 0, 125), pygame.Rect(x, y, 10, 38))
            pygame.draw.line(self.screen, (0, 0, 0), (x, y), (x + 10, y), 2)
            y += 38

    def engine(self):
        if len(self.actors) > 0:
            for l in range(len(self.actors)):
                self.pos_array[l] = (
                    self.actors[l][0].x, self.actors[l][0].y, self.actors[l][0].side, self.actors[l][0].array_position)
            for item in self.actors:

                if item[1] == 0:
                    flag = item[0].dino(self.pos_array, self.actors)
                if item[1] == 1:
                    flag = item[0].rockman(self.pos_array, self.actors)
                if item[1] == 2:
                    flag = item[0].droid(self.pos_array, self.actors)
                if flag != None:
                    self.actors[flag][0].health(item[0].char_attack)

    def draw(self, selected):
        if selected[-1] == '1':
            side = 1
        else:
            side = 0
        if side == 1:
            selected = selected[0:-1]

        pygame.draw.rect(self.screen, (255, 255, 255),
                         pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 80, 80))  # blank space
        if side == 0:
            pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(100, 0, 275, 400), 4)  # space
            pygame.draw.rect(self.screen, (255, 0, 0),
                             pygame.Rect(self.gloss[selected][1], self.gloss[selected][2], 80, 80), 4)  # card
            self.screen.blit(self.char_bg[self.gloss[selected][0]], pygame.mouse.get_pos())

        if side == 1:
            pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(425, 0, 275, 400), 4)
            pygame.draw.rect(self.screen, (255, 0, 0),
                             pygame.Rect(self.gloss[selected][1] + 700, self.gloss[selected][2], 80, 80), 4)  # card
            self.screen.blit(pygame.transform.flip(self.char_bg[self.gloss[selected][0]], True, False),
                             pygame.mouse.get_pos())

        if pygame.mouse.get_pressed()[0] == 1:
            self.pos = pygame.mouse.get_pos()
            if self.pos[0] > 100 and self.pos[0] < 700:
                self.index = len(self.actors)
                if selected == 'dino':
                    self.actors.append(((dino.Dino(self.pos[0], self.pos[1], self.screen, self.index, side)), 0))
                if selected == 'rockman':
                    self.actors.append(((rockman.Rockman(self.pos[0], self.pos[1], self.screen, self.index, side)), 1))
                if selected == 'droid':
                    self.actors.append(((droid.Droid(self.pos[0], self.pos[1], self.screen, self.index, side)), 2))

    def click(self):
        if pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 0 and pos[0] <= 100 and pos[1] >= 10 and pos[1] <= 90:
                self.pre_selected = 'dino'
                return 'dino'
            if pos[0] >= 700 and pos[0] <= 800 and pos[1] >= 10 and pos[1] <= 90:
                self.pre_selected = 'dino1'
                return 'dino1'
            if pos[0] >= 0 and pos[0] <= 100 and pos[1] >= 110 and pos[1] <= 190:
                self.pre_selected = 'rockman'
                return 'rockman'
            if pos[0] >= 700 and pos[0] <= 800 and pos[1] >= 110 and pos[1] <= 190:
                self.pre_selected = 'rockman1'
                return 'rockman1'
            if pos[0] >= 0 and pos[0] <= 100 and pos[1] >= 210 and pos[1] <= 290:
                self.pre_selected = 'droid'
                return 'droid'
            if pos[0] >= 700 and pos[0] <= 800 and pos[1] >= 210 and pos[1] <= 290:
                self.pre_selected = 'droid1'
                return 'droid1'
            if pos[0] >= 100 and pos[0] <= 700 and pos[1] >= 0 and pos[1] <= 400:
                temp = self.pre_selected
                self.pre_selected = ''
                return temp
            else:
                return self.pre_selected

        else:
            return self.pre_selected

    def cards(self):
        y = 10
        for flag in range(3):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(10, y, 80, 80))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(10, y, 80, 80), 1)
            self.screen.blit(self.char_bg[flag], (10, y))
            self.elixer_bar(95, 10)
            y += 100

        y = 10
        for flag in range(3):
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(710, y, 80, 80))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(710, y, 80, 80), 1)
            self.screen.blit(pygame.transform.flip(self.char_bg[flag], True, False), (710, y))
            self.elixer_bar(695, 10)
            y += 100

    def run(self):
        self.screen.fill((255, 255, 255))
        self.home_window()

        while self.running:
            self.drawWindow()
            self.cards()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            selected = self.click()
            if selected != '':
                self.draw(selected)
            self.engine()
            print(self.pos_array)
            pygame.display.update()
            pygame.time.delay(200)


do = Main()
do.run()
