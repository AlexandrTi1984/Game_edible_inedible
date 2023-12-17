import pygame
import random
from os import path
import time

WIDTH = 800  # ширина игрового окна
HEIGHT = 650 # высота игрового окна
FPS = 30 # частота кадров в секунду
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
My_fon = (252,247,247)
#My_fon = (246,239,231)
# настройка папки ассетов
img_dir = path.join(path.dirname(__file__),'img')
snd_dir = path.join(path.dirname(__file__),'snd')
font_name = pygame.font.match_font('arial')
#game_over = False
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.title = None
        self.font = pygame.font.SysFont("Courier New", 30)
        self.background_color = (WHITE)
        self.image1 = None
        self.image2 = None
        self.question_E_nE = None
        self.answer_E_ne_left = None
        self.answer_E_ne_right= None
        self.count_Question = 0
        self.accurancy_answer = 0

    def message(self, number):
        #screen.blit(my_list['logo'][0], (6, 45))
        if number == 1:
            screen.blit(my_list['logo'][0], (6, 45))
            sound_1.play()
        elif number == 0:
            screen.blit(my_list['logo'][1], (6, 45))
            sound_0.play()
    def move (self, pos):
        try:
            x, y = int(pos[0]),int(pos[1])
        except:
            print('Click inside the table only')
        if int(pos[0]) in range (50,300):
            if self.answer_E_ne_left == self.question_E_nE:
                my_list['my_answer'].append(1)
                player1.accurancy_answer +=1
                sound_2.play()
                time.sleep(4)
            else:
                my_list['my_answer'].append(0)
                sound_3.play()
                time.sleep(4)
        elif int(pos[0]) in range(400, 670):
            if self.question_E_nE == self.answer_E_ne_right:
                player1.accurancy_answer += 1
                my_list['my_answer'].append(1)
                sound_2.play()
                time.sleep(4)
            else:
                my_list['my_answer'].append(0)
                sound_3.play()
                time.sleep(4)
        self.print_results()
    def print_results(self):
        for i in range(player1.count_Question):
            if my_list['my_answer'][i] == 1:
                screen.blit(my_list['answer'][1], (2 + i * 80, 545))
            if my_list['my_answer'][i] == 0:
                screen.blit(my_list['answer'][0], (2 + i * 80, 545))

    def show_start_screen(self):
        background = pygame.image.load(path.join(img_dir, 'fon2.jpg')).convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        pygame.display.flip()
    def show_end_screen(self):  # экран окончания игры + начало игры + рекорды
        #screen.fill(BLACK)
        background = pygame.image.load(path.join(img_dir,'kubok.png')).convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background_rect = background.get_rect()
        screen.blit(background, background_rect)

        my_string = 'Правильных ответов: ' + str(self.accurancy_answer) + ' из 8'
        font = pygame.font.Font(font_name, 60)
        text_surface = font.render(my_string, True, BLUE)
        screen.blit(text_surface,(70,HEIGHT - 70))
        pygame.display.flip()
        time.sleep(1)
        #running = False
        pygame.quit()

# создаем игру и окно
pygame.init()
pygame.mixer.init() # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
clock = pygame.time.Clock()
# all_sprites =pygame.sprite.Group()
player1 = Player()

# all_sprites.add(player1)
#Делаем словарь со списком фоток
my_list={}
my_list['edible']=[]
my_list['Non_edible']=[]
my_list['logo']=[]
my_list['answer']=[]
my_list['my_answer']=[]

img = pygame.image.load(path.join(img_dir, 'logo1.png')).convert()
img.set_colorkey(WHITE)
my_list['logo'].append(img)
img = pygame.image.load(path.join(img_dir, 'logo2.png')).convert()
img.set_colorkey(WHITE)
my_list['logo'].append(img)

img = pygame.image.load(path.join(img_dir, 'no_small.png')).convert()
img.set_colorkey(WHITE)
my_list['answer'].append(img)
img = pygame.image.load(path.join(img_dir, 'yes_small.png')).convert()
img.set_colorkey(WHITE)
my_list['answer'].append(img)
#Добавляем звук
sound_0 = pygame.mixer.Sound(path.join(snd_dir,'sound0.mp3'))
sound_1 = pygame.mixer.Sound(path.join(snd_dir,'sound1.mp3'))
sound_2 = pygame.mixer.Sound(path.join(snd_dir,'sound2.mp3'))
sound_3 = pygame.mixer.Sound(path.join(snd_dir,'sound3.mp3'))

for i in range(12):
    filename = 'n{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(WHITE)
    img = pygame.transform.scale(img,(250,250))
    my_list['Non_edible'].append(img)
    filename = 's{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(WHITE)
    img = pygame.transform.scale(img,(250,250))
    my_list['edible'].append(img)
# Игровой Цикл игры
running = True
Upload_picture = False
while running :
#while running and player1.count_Question <= 8:

    # держим цикл на правильной скорости
    clock.tick(FPS)
    if player1.count_Question == 8:
         game_over = True
         running = False
         player1.show_end_screen()
    # else:
            # Ввод процесса (события) 0 - не сьедобное, 1 - сьедобное
    if Upload_picture == False:
        player1.show_start_screen()
        player1.question_E_nE = random.randint(0, 1)
        player1.message(player1.question_E_nE)
        player1.image1 = random.choice(my_list['edible'])
        player1.image2 = random.choice(my_list['Non_edible'])
        side = random.randint(0, 1)
        if player1.count_Question>0:
            player1.print_results()
        # Делаем рандом стороны сьедобное - несьедобное
        if side == 1:
            screen.blit(player1.image1, (50, 150))
            screen.blit(player1.image2, (410, 150))
            player1.answer_E_ne_left = 1
            player1.answer_E_ne_right = 0
        elif side == 0:
            screen.blit(player1.image2, (50, 150))
            screen.blit(player1.image1, (410, 150))
            player1.answer_E_ne_left = 0
            player1.answer_E_ne_right = 1
        else:
            print('Error при загрузки изображения')

        Upload_picture = True
        player1.print_results()

        # Закрытие окна
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Upload_picture = False
            player1.count_Question += 1
            player1.move(event.pos)
            player1.print_results()

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    # Визуализация (сборка)

pygame.quit()