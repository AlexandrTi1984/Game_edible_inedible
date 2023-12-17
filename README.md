
# Game edible inedible 

Children's game edible inedible written using "pygame". 

🍎🍒🥖  vs 🔨🏠🐯


## Installation libraries:

```python
pip install pygame
```
    
## Screenshots

![App Screenshot](pic1.gif)




## Usage/Examples

```python
import pygame
import random
from os import path
import time

....
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
...
```
