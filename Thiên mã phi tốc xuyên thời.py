import pygame

from random import randint

import os


pygame.mixer.init()
pygame.init()
pygame.display.set_caption('Thiên mã phi tốc xuyên thời')

screen = pygame.display.set_mode((1000, 775))

# Khai báo giá trị từng ô trên bàn cờ

running = True

# Khai báo link ảnh trong máy
PINK = (255, 102, 153)
WHITE = (255, 255, 255)
GREY = (89, 89, 89)
BLACK = (0, 0, 0) 
BLUE = (12, 192, 223)
YELLOW = (255, 222, 89)
GREEN = (126, 217, 87)
RED = (255, 49, 49)


background = "IN GAME.png"
end_game_menu = "END_GAME_menu.png"


blue_seahorse = "SEAHORSE_BLUE.png"
green_seahorse = "SEAHORSE_GREEN.png"
yellow_seahorse = "SEAHORSE_YELLOW.png"
red_seahorse = "SEAHORSE_RED.png"


blue_seahorse_55X55 = "SEAHORSE_BLUE_55X55.png"
green_seahorse_55X55 = "SEAHORSE_GREEN_55X55.png"
yellow_seahorse_55X55 = "SEAHORSE_YELLOW_55X55.png"
red_seahorse_55X55 = "SEAHORSE_RED_55X55.png"


dice = "dice.png"
dice_1_1x = "dice_1.1x.png"
menu = "WELCOME.png"
back_icon_white = "RETURN_1.png"
back_icon = "RETURN_2.png"


instruc = "INSTRUCTION.png"
new_game = "NEW GAME.png"
how_to_play = "HOW TO PLAY.png"
quit_image = "QUIT.png"
new_game_white = "NEW GAME_2.png"
quit_image_white = "QUIT_2.png"
how_to_play_white = "HOW TO PLAY_2.png"
end_game = "END GAME.png"
end_game_2 = "END GAME_2.png"


blue_turn = "BLUE TURN.png"
yellow_turn = "YELLOW TURN.png"
green_turn = "GREEN TURN.png"
red_turn = "RED TURN.png"

blue_win = "BLUE.png"
yellow_win = "YELLOW.png"
green_win = "GREEN.png"
red_win = "RED.png"

Pickleball = pygame.mixer.Sound("Pickleball.wav")
BUTTON_1 = pygame.mixer.Sound("BUTTON.wav")
BUTTON_2 = pygame.mixer.Sound("CARTOON_BUTTON.wav")




# Khai báo các ảnh
image_menu = pygame.image.load(menu)
image_end_game_menu = pygame.image.load(end_game_menu)
image_back_white = pygame.image.load(back_icon_white)
image_back = pygame.image.load(back_icon)
image_instruc = pygame.image.load(instruc)
image_background = pygame.image.load(background)


image_newgame = pygame.image.load(new_game)
image_how_to_play = pygame.image.load(how_to_play)
image_quit = pygame.image.load(quit_image)
image_newgame_white = pygame.image.load(new_game_white)
image_how_to_play_white = pygame.image.load(how_to_play_white)
image_quit_white = pygame.image.load(quit_image_white)
image_end_game = pygame.image.load(end_game_2)
image_end_game_white = pygame.image.load(end_game)


image_blue_turn = pygame.image.load(blue_turn)
image_yellow_turn = pygame.image.load(yellow_turn)
image_green_turn = pygame.image.load(green_turn)
image_red_turn = pygame.image.load(red_turn)


image_seahorse = [None] * 4
image_seahorse[0] = pygame.image.load(blue_seahorse)
image_seahorse[1] = pygame.image.load(yellow_seahorse)
image_seahorse[2] = pygame.image.load(green_seahorse)
image_seahorse[3] = pygame.image.load(red_seahorse)



image_seahorse_55X55 = [None] * 4
image_seahorse_55X55[0] = pygame.image.load(blue_seahorse_55X55)
image_seahorse_55X55[1] = pygame.image.load(yellow_seahorse_55X55)
image_seahorse_55X55[2] = pygame.image.load(green_seahorse_55X55)
image_seahorse_55X55[3] = pygame.image.load(red_seahorse_55X55)


image_dice = pygame.image.load(dice)
image_dice_1_1x = pygame.image.load(dice_1_1x)

image_blue_win = pygame.image.load(blue_win)
image_yellow_win = pygame.image.load(yellow_win)
image_green_win = pygame.image.load(green_win)
image_red_win = pygame.image.load(red_win)

point = [0] * 16
point_blue = 0
point_yellow = 0
point_green = 0
point_red = 0


class Position:
    def __init__(self, x, y, pos, cage, finish, finish_check):
        self.x = x
        self.y = y
        self.pos = pos
        self.cage = cage
        self.finish = finish
        self.finish_check = finish_check
    
seahorse =  [Position(x = 0, y = 0, pos = -1, cage = 0, finish = 0, finish_check = 0) for _ in range(16)]
start_pos = [Position(x = 0, y = 0, pos = -1, cage = 0, finish = 0, finish_check = 0) for _ in range(16)]

seahorse[0].x = 70
seahorse[0].y = 60
seahorse[1].x = 130
seahorse[1].y = 60
seahorse[2].x = 70
seahorse[2].y = 120
seahorse[3].x = 130
seahorse[3].y = 120

seahorse[4].x = 70
seahorse[4].y = 530
seahorse[5].x = 130
seahorse[5].y = 530
seahorse[6].x = 70
seahorse[6].y = 590
seahorse[7].x = 130
seahorse[7].y = 590

seahorse[8].x = 540
seahorse[8].y = 530
seahorse[9].x = 600
seahorse[9].y = 530
seahorse[10].x = 540
seahorse[10].y = 590
seahorse[11].x = 600
seahorse[11].y = 590

seahorse[12].x = 540
seahorse[12].y = 60
seahorse[13].x = 600
seahorse[13].y = 60
seahorse[14].x = 540
seahorse[14].y = 120
seahorse[15].x = 600
seahorse[15].y = 120

start_pos[0].x = 70
start_pos[0].y = 60
start_pos[1].x = 130
start_pos[1].y = 60
start_pos[2].x = 70
start_pos[2].y = 120
start_pos[3].x = 130
start_pos[3].y = 120

start_pos[4].x = 70
start_pos[4].y = 530
start_pos[5].x = 120
start_pos[5].y = 530
start_pos[6].x = 70
start_pos[6].y = 590
start_pos[7].x = 120
start_pos[7].y = 590

start_pos[8].x = 540
start_pos[8].y = 530
start_pos[9].x = 580
start_pos[9].y = 530
start_pos[10].x = 540
start_pos[10].y = 590
start_pos[11].x = 580
start_pos[11].y = 590

start_pos[12].x = 540
start_pos[12].y = 60
start_pos[13].x = 600
start_pos[13].y = 60
start_pos[14].x = 540
start_pos[14].y = 120
start_pos[15].x = 600
start_pos[15].y = 120




data = [
        [0, 245, 20], #0
        [1, 245, 60], #1
        [2, 245, 110],#2
        [3, 245, 155],#3
        [4, 245, 200],#4
        [5, 245, 245],#5
        [6, 200, 245],#6
        [7, 155, 245],#7
        [8, 110, 245],#8
        [9, 65, 245], #9
        [10, 20, 245],#10
        [11, 20, 345],#11
        [12, 20, 425],#12


        [13, 65, 425], #13
        [14, 110, 425],#14
        [15, 155, 425],#15
        [16, 200, 425],#16
        [17, 245, 425],#17
        [18, 245, 470],#18
        [19, 245, 515],#19
        [20, 245, 560],#20
        [21, 245, 605],#21
        [22, 245, 650],#22
        [23, 340, 650],#23
        [24, 420, 650],#24


        [25, 420, 605],#25
        [26, 420, 560],#26
        [27, 420, 515],#27
        [28, 420, 470],#28
        [29, 420, 425],#29
        [30, 470, 425],#30
        [31, 515, 425],#31
        [32, 560, 425],#32
        [33, 605, 425],#33
        [34, 650, 425],#34
        [35, 650, 340],#35
        [36, 655, 245],#36


        [37, 610, 245],#37
        [38, 565, 245],#38
        [39, 520, 245],#39
        [40, 475, 245],#40
        [41, 425, 245],#41
        [42, 425, 200],#42
        [43, 425, 155],#43
        [44, 425, 112],#44
        [45, 425, 60], #45
        [46, 425, 20], #46
        [47, 340, 20], #47


        [100, 340, 20], #B0
        [101, 335, 65], #B1
        [102, 335, 105],#B2
        [103, 335, 145],#B3
        [104, 335, 185],#B4
        [105, 335, 225],#B5
        [106, 335, 265],#B6


        [200, 20, 345], #Y0
        [201, 70, 340], #Y1
        [202, 110, 340],#Y2
        [203, 150, 340],#Y3
        [204, 190, 340],#Y4
        [205, 230, 340],#Y5
        [206, 270, 340],#Y6


        [300, 340, 650],#G0
        [301, 335, 605],#G1
        [302, 335, 565],#G2
        [303, 335, 525],#G3
        [304, 335, 485],#G4
        [305, 335, 445],#G5
        [306, 335, 405],#G6


        [400, 655, 340],#R0
        [401, 600, 340],#R1
        [402, 560, 340],#R2
        [403, 520, 340],#R3
        [404, 480, 340],#R4
        [405, 440, 340],#R5
        [406, 400, 340],#R6

    ]

max_pos = [100] * 16
max_pos[0] = 47
max_pos[1] = 47
max_pos[2] = 47
max_pos[3] = 47

place_color = [-1] * 500

chess_num = [0] * 5
place = [0] * 500

def Game_func():
    
    pygame.init()
    global running
    global event
    global point
    global point_blue
    global point_yellow
    global point_green
    global point_red

    pygame.mixer.music.stop()

    font = pygame.font.SysFont('sans', 70)
    font_text = pygame.font.SysFont('sans', 30)

    turn = 0
    check_turn = turn


    dice_num = 0
    num = 0


    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos() 

        screen.blit(image_background, (0, 0))
        screen.blit(image_dice, (765, 515))
        screen.blit(image_end_game_white, (700, 720))


        if (765 < mouse_x  < 965) and (515 < mouse_y < 680):
            screen.blit(image_dice_1_1x, (705, 465))

        if (705 < mouse_x  < 1000) and (720 < mouse_y < 770):
            screen.blit(image_end_game, (700, 720))

        for chess_number in range (0, 16):
            if(seahorse[chess_number].x <= mouse_x <= seahorse[chess_number].x + 50 and seahorse[chess_number].y <= mouse_y <= seahorse[chess_number].y + 50):
                screen.blit(image_seahorse_55X55[(chess_number // 4)], (seahorse[chess_number].x - 5, seahorse[chess_number].y - 5))
            else: 
                screen.blit(image_seahorse[(chess_number // 4)], (seahorse[chess_number].x, seahorse[chess_number].y))
        
        point_str_blue = str(point_blue)
        point_str_yellow = str(point_yellow)
        point_str_green = str(point_green)
        point_str_red = str(point_red)

        point_text_blue = font.render(point_str_blue, True, WHITE)
        point_text_yellow = font.render(point_str_yellow, True, WHITE)
        point_text_green = font.render(point_str_green, True, WHITE)
        point_text_red = font.render(point_str_red, True, WHITE)

        screen.blit(point_text_blue, (880, 195))
        screen.blit(point_text_yellow, (880, 265))
        screen.blit(point_text_green, (880, 335))
        screen.blit(point_text_red, (880, 410))
        
        # In ra giá trị của tọa độ x y
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if check_turn != turn:
            check_turn = turn

        if(turn == 0) : screen.blit(image_blue_turn, (720, 25))
        if(turn == 1) : screen.blit(image_yellow_turn, (720, 25))
        if(turn == 2) : screen.blit(image_green_turn, (720, 25))
        if(turn == 3) : screen.blit(image_red_turn, (720, 25))
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                BUTTON_1.play()
                if (705 < mouse_x  < 1000) and (720 < mouse_y < 770):
                    final_menu(point_blue, point_yellow, point_green, point_red)
                
                if (705 < mouse_x  < 985) and (465 < mouse_y < 680):
                    
                    dice_num = randint(1,6)
                    dice_result = str(dice_num)
                    
                    dice_num_text = font.render(dice_result, True, BLACK)
                    screen.blit(dice_num_text, (345, 325))
                    
                    pygame.display.flip()  
                    pygame.time.delay(1000)
                    BUTTON_1.stop()
                    if chess_num[turn] == 0:
                        if (dice_num != 6):
                            turn = (turn + 1) % 4
                            continue
                    
                    possible_check = 0     
                    for k in range (0, 4):
                        check = turn_possible((turn * 4) + k, dice_num)
                        if check == 1:
                            possible_check = 1

                    if possible_check == 0:
                        turn = (turn + 1) % 4
                        continue

        if turn == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    BUTTON_1.play()
                    i = get_seahorse_blue()
                    
                    

        elif turn == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    BUTTON_1.play()
                    i = get_seahorse_yellow()
                    
                    
        
        elif turn == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    BUTTON_1.play()
                    i = get_seahorse_green()
                    

        elif turn == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    BUTTON_1.play()
                    i = get_seahorse_red()
                    
                    
                    
        if i != -1:
            
            if (dice_num == 6 and seahorse[i].cage == 0 and seahorse[i].pos == -1):
                pos = i // 4
                if place[(pos) * 12] == 0: 
                    seahorse[i].x = data[(pos) * 12][1]
                    seahorse[i].y = data[(pos) * 12][2]
                    chess_num[pos] = chess_num[pos] + 1
                    seahorse[i].pos = pos * 12
                    place[seahorse[i].pos] = 1
                    seahorse[i].cage = 1
                    dice_num = 0
                    continue

                elif place[pos * 12] != 0: 
                    continue
                
            
            num = seahorse[i].pos
            

            if seahorse[i].finish == 1:
                if seahorse[i].finish_check == 1:
                    if dice_num == seahorse[i].pos - (100 * ((i // 4) + 1)) + 1:
                        seahorse[i].pos = (100 * ((i // 4) + 1)) + dice_num
                else:
                    seahorse[i].pos = (100 * ((i // 4) + 1)) + dice_num
                place[(100 * ((i // 4) + 1)) + dice_num] = 1
            
            if seahorse[i].pos > ((i // 4) + 1) * 100:
                seahorse[i].finish_check = 1

            elif seahorse[i].finish == 0:
                if (seahorse[i].cage == 1):
                    if seahorse[i].pos + dice_num <= max_pos[i]:
                        
                        num = seahorse[i].pos
                        
                        place[seahorse[i].pos] = 0
                        
                        if 0 <= i <= 3:
                            if 0 <= 12 - seahorse[i].pos and 12 - seahorse[i].pos <= dice_num or 0 <= 24 - seahorse[i].pos and 24 - seahorse[i].pos <= dice_num or 0 <= 36 - seahorse[i].pos and 36 - seahorse[i].pos <= dice_num:
                                seahorse[i].pos = seahorse[i].pos + 1


                        elif 4 <= i <= 7:
                            if 0 <= 48 - seahorse[i].pos and 48 - seahorse[i].pos <= dice_num or 0 <= 24 - seahorse[i].pos and 24 - seahorse[i].pos <= dice_num or 0 <= 36 - seahorse[i].pos and 36 - seahorse[i].pos <= dice_num:
                                seahorse[i].pos = seahorse[i].pos + 1


                        elif 8 <= i <= 11:
                            if 0 <= 12 - seahorse[i].pos and 12 - seahorse[i].pos <= dice_num or 0 <= 48 - seahorse[i].pos and 48 - seahorse[i].pos <= dice_num or 0 <= 36 - seahorse[i].pos and 36 - seahorse[i].pos <= dice_num:
                                seahorse[i].pos = seahorse[i].pos + 1


                        elif 12 <= i <= 15:
                            if 0 <= 12 - seahorse[i].pos and 12 - seahorse[i].pos <= dice_num or 0 <= 24 - seahorse[i].pos and 24 - seahorse[i].pos <= dice_num or 0 <= 48 - seahorse[i].pos and 48 - seahorse[i].pos <= dice_num:
                                seahorse[i].pos = seahorse[i].pos + 1


                        if (seahorse[i].pos + dice_num) > 47 and i >= 4:
                            max_pos[i] = ((i // 4) * 12) - 1


                        seahorse[i].pos = (seahorse[i].pos + dice_num) % 48
                    

            if place[seahorse[i].pos] == 1 and place_color[seahorse[i].pos] == (i // 4):
                seahorse[i].pos = num
                continue
            elif seahorse[i].pos - (100 * ((i // 4) + 1)) > dice_num:
                continue

            test = 1
            pos = -1
            if place[seahorse[i].pos] == 1 and place_color[seahorse[i].pos] != (i // 4):
                for j in range(0, 16):
                    if seahorse[j].pos == seahorse[i].pos and j != i and test == 1:
                        seahorse[j].pos = -1
                        seahorse[j].cage = 0

                        if (j // 4) == 0:
                            point_blue = point_blue - point[j]
                            max_pos[j] = 47
                        if (j // 4) == 1:
                            point_yellow = point_yellow - point[j]
                        if (j // 4) == 2:
                            point_green = point_green - point[j]
                        if (j // 4) == 3:
                            point_red = point_red - point[j]

                        point[j] = 0
                        seahorse[i].finish = 0
                        max_pos[j] = 100
                        seahorse[j].x = start_pos[j].x
                        seahorse[j].y = start_pos[j].y
                        
                        pos = j
                        place[seahorse[j].pos] = 0
                        test = 0
            chess_num[(pos // 4)] = chess_num[(pos // 4)] - 1
            if seahorse[i].pos == max_pos[i]:
                        seahorse[i].finish = 1
            for row in data:
                if row[0] == seahorse[i].pos:
                    seahorse[i].x = row[1]
                    seahorse[i].y = row[2]
                    place[seahorse[i].pos] = 1
                    place[num] = 0
                    place_color[seahorse[i].pos] = (i // 4)
                    
                    if seahorse[i].pos >= (100 * ((i // 4) + 1) + 1):
                        point[i] = 44 + dice_num * dice_num
                    else:
                        point[i] = point[i] + dice_num

                    if (i // 4) == 0:
                        point_blue = point_counter(0, 4)
                    if (i // 4) == 1:
                        point_yellow = point_counter(4, 8)
                    if (i // 4) == 2:
                        point_green = point_counter(8, 12)
                    if (i // 4) == 3:
                        point_red = point_counter(12, 16)
                    if dice_num != 6:
                        turn = (turn + 1) % 4
                    dice_num = 0
                    
                    continue

        pygame.display.update()            
        pygame.display.flip()

        
def get_seahorse_blue():
    mouse_x, mouse_y = pygame.mouse.get_pos()  
    i = -1             
    if (seahorse[0].x - 10 < mouse_x < seahorse[0].x + 60) and (seahorse[0].y - 10 < mouse_y < seahorse[0].y + 60):
        i = 0
    elif (seahorse[1].x - 10 < mouse_x < seahorse[1].x + 60) and (seahorse[1].y - 10 < mouse_y < seahorse[1].y + 60):
        i = 1
    elif (seahorse[2].x - 10 < mouse_x < seahorse[2].x + 60) and (seahorse[2].y - 10 < mouse_y < seahorse[2].y + 60):
        i = 2
    elif (seahorse[3].x - 10 < mouse_x < seahorse[3].x + 60) and (seahorse[3].y - 10 < mouse_y < seahorse[3].y + 60):
        i = 3

    return i


def get_seahorse_yellow():
    mouse_x, mouse_y = pygame.mouse.get_pos()  
    i = -1             
    if (seahorse[4].x - 10 < mouse_x < seahorse[4].x + 60) and (seahorse[4].y - 10 < mouse_y < seahorse[4].y + 60):
        i = 4
    elif (seahorse[5].x - 10 < mouse_x < seahorse[5].x + 60) and (seahorse[5].y - 10 < mouse_y < seahorse[5].y + 60):
        i = 5
    elif (seahorse[6].x - 10 < mouse_x < seahorse[6].x + 60) and (seahorse[6].y - 10 < mouse_y < seahorse[6].y + 60):
        i = 6
    elif (seahorse[7].x - 10 < mouse_x < seahorse[7].x + 60) and (seahorse[7].y - 10 < mouse_y < seahorse[7].y + 60):
        i = 7

    return i


def get_seahorse_green():
    mouse_x, mouse_y = pygame.mouse.get_pos()  
    i = -1             
    if (seahorse[8].x - 10 < mouse_x < seahorse[8].x + 60) and (seahorse[8].y - 10 < mouse_y < seahorse[8].y + 60):
        i = 8
    elif (seahorse[9].x - 10 < mouse_x < seahorse[9].x + 60) and (seahorse[9].y - 10 < mouse_y < seahorse[9].y + 60):
        i = 9
    elif (seahorse[10].x - 10 < mouse_x < seahorse[10].x + 60) and (seahorse[10].y - 10 < mouse_y < seahorse[10].y + 60):
        i = 10
    elif (seahorse[11].x - 10 < mouse_x < seahorse[11].x + 60) and (seahorse[11].y - 10 < mouse_y < seahorse[11].y + 60):
        i = 11

    return i


def get_seahorse_red():
    mouse_x, mouse_y = pygame.mouse.get_pos()  
    i = -1             
    if (seahorse[12].x - 10 < mouse_x < seahorse[12].x + 60) and (seahorse[12].y - 10 < mouse_y < seahorse[12].y + 60):
        i = 12
    elif (seahorse[13].x - 10 < mouse_x < seahorse[13].x + 60) and (seahorse[13].y - 10 < mouse_y < seahorse[13].y + 60):
        i = 13
    elif (seahorse[14].x - 10 < mouse_x < seahorse[14].x + 60) and (seahorse[14].y - 10 < mouse_y < seahorse[14].y + 60):
        i = 14
    elif (seahorse[15].x - 10 < mouse_x < seahorse[15].x + 60) and (seahorse[15].y - 10 < mouse_y < seahorse[15].y + 60):
        i = 15

    return i


def point_counter(n, m):
    global point
    return_point = 0
    for i in range(n, m):
        return_point = return_point + point[i]

    return return_point


def turn_possible(i, dice_num):
    global max_pos
    global seahorse
    global place
    global place_color
    global chess_num
    if seahorse[i].cage == 0:
        if dice_num == 6 and place[(i // 4) * 12] == 0 and seahorse[i].pos == -1:
            return 1
    if seahorse[i].cage != 0:
        if seahorse[i].pos + dice_num <= max_pos[i]:
            if place[seahorse[i].pos + dice_num] == 1:
                if place_color[seahorse[i].pos + dice_num] != i // 4:
                    return 1
            elif place[seahorse[i].pos + dice_num] != 1:
                return 1
        if seahorse[i].finish == 1:
            if place[(100 * ((i // 4) + 1)) + dice_num] != 1:
                return 1
            if(seahorse[i].finish_check == 1):
                if place[seahorse[i].pos + dice_num] != 1:
                    if dice_num > seahorse[i].pos - (100 * ((i // 4)+1)) and seahorse[i].pos + dice_num <= 6 + (100 * ((i // 4)+1)):
                        return 1

        
    return 0


def final_menu(a, b, c, d):
    max_value = max(a, b, c, d)
    global running
    global event
    pygame.mixer.music.load("BOOYAH_FINAL.wav")
    pygame.mixer.music.play(-1)
    pygame.init()
    point_result = str(max_value)
    font = pygame.font.SysFont('sans', 80)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(image_end_game_menu, (0 , 0))
        if max_value == a:
            screen.blit(image_blue_win, (500 , 230))
            point_result_text = font.render(point_result, True, BLUE)

        elif max_value == b:
            screen.blit(image_yellow_win, (500 , 230))
            point_result_text = font.render(point_result, True, YELLOW)

        elif max_value == c:
            screen.blit(image_green_win, (500 , 230))
            point_result_text = font.render(point_result, True, GREEN)

        elif max_value == d:
            screen.blit(image_red_win, (500 , 230))
            point_result_text = font.render(point_result, True, RED)
        
                    
        
        screen.blit(point_result_text, (570, 310))
        pygame.display.update()            
        pygame.display.flip()




def Instruc_func():
    global running
    global event
    pygame.init()
    #pygame.mixer.music.stop()
    while running:

        #  Tạo hình giao diện chơi game
        
        screen.blit(image_instruc, (0, 0))   
        # In ra giá trị của tọa độ x y
        mouse_x, mouse_y = pygame.mouse.get_pos()  
        #  Vòng lặp in hình liên tục
        screen.blit(image_back_white, (660, 645))
        if (660 < mouse_x < 920) and (640 < mouse_y < 690) :
            screen.blit(image_back, (660, 645))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                BUTTON_2.play()
                if (660 < mouse_x < 920) and (640 < mouse_y < 690) : 
                    Menu_func()
                    BUTTON_2.stop()
                    break

        pygame.display.update()            
        pygame.display.flip()



def Menu_func():
    global running
    global event
    pygame.mixer.music.load("Pickleball.wav")
    pygame.mixer.music.play(-1)
    while running:

        #  Tạo hình giao diện chơi game
        screen.blit(image_menu, (0, 0))

        # In ra giá trị của tọa độ x y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #  Vòng lặp in hình liên tục
        screen.blit(image_newgame_white, (350, 495))
        screen.blit(image_how_to_play_white, (350, 565))
        screen.blit(image_quit_white, (350, 635))
        if (360 < mouse_x < 650) and (490 < mouse_y < 550) : 
            screen.blit(image_newgame, (350, 495))

        if (360 < mouse_x < 650) and (560 < mouse_y < 620) : 
            screen.blit(image_how_to_play, (350, 565))

        if (360 < mouse_x < 650) and (630 < mouse_y < 690) : 
            screen.blit(image_quit, (350, 635))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                BUTTON_2.play()
                if (360 < mouse_x < 650) and (490 < mouse_y < 550) : 
                    Game_func()
                    BUTTON_2.stop()
                    break
                elif (360 < mouse_x < 650) and (560 < mouse_y < 620) : 
                    Instruc_func()
                    BUTTON_2.stop()
                    break
                elif (360 < mouse_x < 650) and (630 < mouse_y < 690) :
                    BUTTON_2.stop()
                    running = False
        
        pygame.display.update()            
        pygame.display.flip()


Menu_func()
    
pygame.quit()

    
