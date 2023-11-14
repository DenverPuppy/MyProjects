import pygame
import random

pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pos_x = WIDTH / 4
pos_y = (0.1 * HEIGHT)
rec_width = WIDTH - 0.5 * WIDTH
rec_height = HEIGHT - 0.2 * HEIGHT
sector_width = rec_width/3
sector_height = rec_height/3

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
other = (211,30,24)


clicked = [0,0,0,0,0,0,0,0,0]
symbol = ["","","","","","","","",""]

line1_list = [[(pos_x, pos_y), (pos_x+sector_width, pos_y+sector_height)], [(pos_x+sector_width, pos_y), (pos_x+sector_width*2, pos_y+sector_height)], [(pos_x+sector_width*2, pos_y), (pos_x+sector_width*3, pos_y+sector_height)],
              [(pos_x, pos_y+sector_height), (pos_x+sector_width, pos_y+sector_height*2)], [(pos_x+sector_width, pos_y+sector_height), (pos_x+sector_width*2, pos_y+sector_height*2)], [(pos_x+sector_width*2, pos_y+sector_height), (pos_x+sector_width*3, pos_y+sector_height*2)],
              [(pos_x, pos_y+sector_height*2), (pos_x+sector_width, pos_y+sector_height*3)], [(pos_x+sector_width, pos_y+sector_height*2), (pos_x+sector_width*2, pos_y+sector_height*3)], [(pos_x+sector_width*2, pos_y+sector_height*2), (pos_x+sector_width*3, pos_y+sector_height*3)]]

line2_list =  [[(pos_x, pos_y+sector_height), (pos_x+sector_width, pos_y)], [(pos_x+sector_width, pos_y+sector_height), (pos_x+sector_width*2, pos_y)], [(pos_x+sector_width*2, pos_y+sector_height), (pos_x+sector_width*3, pos_y)],
               [(pos_x, pos_y+sector_height*2), (pos_x+sector_width, pos_y+sector_height)], [(pos_x+sector_width, pos_y+sector_height*2), (pos_x+sector_width*2, pos_y+sector_height)], [(pos_x+sector_width*2, pos_y+sector_height*2), (pos_x+sector_width*3, pos_y+sector_height)],
               [(pos_x, pos_y+sector_height*3), (pos_x+sector_width, pos_y+sector_height*2)], [(pos_x+sector_width, pos_y+sector_height*3), (pos_x+sector_width*2, pos_y+sector_height*2)], [(pos_x+sector_width*2, pos_y+sector_height*3), (pos_x+sector_width*3, pos_y+sector_height*2)]]


circle_list =  [(pos_x+sector_width/2, pos_y+sector_height/2), (pos_x+sector_width/2*3, pos_y+sector_height/2), (pos_x+sector_width/2*5, pos_y+sector_height/2),
                (pos_x+sector_width/2, pos_y+sector_height/2*3), (pos_x+sector_width/2*3, pos_y+sector_height/2*3), (pos_x+sector_width/2*5, pos_y+sector_height/2*3),
                (pos_x+sector_width/2, pos_y+sector_height/2*5), (pos_x+sector_width/2*3, pos_y+sector_height/2*5), (pos_x+sector_width/2*5, pos_y+sector_height/2*5)]

win_list_row =  [[(pos_x, pos_y+sector_height/2), (pos_x+sector_width*3, pos_y+sector_height/2)],
                 [(pos_x, pos_y+sector_height*3/2), (pos_x+sector_width*3, pos_y+sector_height*3/2)],
                 [(pos_x, pos_y+sector_height*5/2), (pos_x+sector_width*3, pos_y+sector_height*5/2)]]

win_list_col =  [[(pos_x+sector_width/2, pos_y), (pos_x+sector_width/2, pos_y+sector_height*3)],
                 [(pos_x+sector_width*3/2, pos_y), (pos_x+sector_width*3/2, pos_y+sector_height*3)],
                 [(pos_x+sector_width*5/2, pos_y), (pos_x+sector_width*5/2, pos_y+sector_height*3)]]
win_list_diag = [[(pos_x, pos_y), (pos_x+sector_width*3, pos_y+sector_height*3)],
                 [(pos_x, pos_y+sector_height*3), (pos_x+sector_width*3, pos_y)]]

mouse_range = line1_list[:]

turn = random.randint(1,10)

def get_turn():
    if turn >= 5:
        temp_state = False
    else:
        temp_state = True
    return temp_state

state = get_turn()


def highlits():
    if state == False:
        pygame.draw.lines(screen, white, True, ((pos_x/4,pos_y+60), (pos_x/4+138,pos_y+60)), 5)
    elif state == True:
        pygame.draw.lines(screen, white, True, ((pos_x*3 + pos_x/4,pos_y+60),(pos_x*3 + pos_x/4 + 138,pos_y+60)), 5)

def player_text():
    points1 = 0
    points1 = str(points1)
    points2 = 0
    points2 = str(points2)
    text_font = pygame.font.SysFont("Impact", 40)
    score_font = pygame.font.SysFont("Impact", 120)

    score1 = score_font.render(points1, True, white)
    score2 = score_font.render(points2, True, white)

    player1 = text_font.render("PLAYER 1", True, white)
    player2 = text_font.render("PLAYER 2", True, white)


    screen.blit(player1, (pos_x/4,pos_y))
    screen.blit(player2, (pos_x*3 + pos_x/4,pos_y))
    screen.blit(score1, (pos_x/3 + pos_x/12 , pos_y*4))
    screen.blit(score2, (pos_x*3 + pos_x/3 + pos_x/12, pos_y * 4))



def mouse_click():
    global state
    global loop
    position = pygame.mouse.get_pos()

    for i in range(9):
        if mouse_range[i][0][0] < position[0] < mouse_range[i][1][0] and mouse_range[i][0][1] < position[1] < mouse_range[i][1][1] and clicked[i] == False: #Jeśli jest w obszarze
            if pygame.mouse.get_pressed()[0] == True:   # Jeśli jest wciśnięta myszka
                clicked[i] = True                       # Wpisuje że to pole jest już zajęte
                if state == False:
                    symbol[i] = "x"
                elif state == True:
                     symbol[i] = "o"
                state = not state

def draw_win(input):
    for i in range(3):
        if input == (i,"c"):
            pygame.draw.lines(screen, red, True, win_list_row[i], 10)
        elif input == ("r",i):
            pygame.draw.lines(screen, red, True, win_list_col[i], 10)
        if input == (2,2):
            pygame.draw.lines(screen, red, True, win_list_diag[0], 10)
        elif input == (3,3):
            pygame.draw.lines(screen, red, True, win_list_diag[1], 10)

def draw_symbols():

    for i in range(9):
        if clicked[i] == True and symbol[i] == "x":
            pygame.draw.lines(screen, white, True, line1_list[i], 5)
            pygame.draw.lines(screen, white, True, line2_list[i], 5)
        elif clicked[i] == True and symbol[i] == "o":
            pygame.draw.circle(screen, white, circle_list[i], 100, 4)

def draw_board():

    pygame.draw.rect(screen, white, (pos_x, pos_y, rec_width, rec_height), width=5)
    temp_rectangles = []
    for x in range(3):
        for y in range(3):
            temp_rectangles.append(pygame.draw.rect(screen, white, (pos_x+rec_width/3*x, pos_y+rec_height/3*y,rec_width/3,rec_height/3 ), width=1))
    print(temp_rectangles)
    rectangles = temp_rectangles
    return rectangles


def game(): # Gra
    pygame.init()

    pygame.display.set_caption("TicTacToe")
    clock = pygame.time.Clock()
    done = False


    while done == False:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        draw_board()
        player_text()
        highlits()
        mouse_click()
        draw_symbols()
        rules()
        pygame.display.flip()
        clock.tick(60)
        print(pygame.mouse.get_pos())
    pygame.quit()

def rules():
    for x in range(3):

            #Poziomo
            if symbol[x*3]+symbol[x*3+1]+symbol[x*3+2] == "xxx":
                col = (x,"c")
                draw_win(col)
            elif symbol[x*3]+symbol[x*3+1]+symbol[x*3+2] == "ooo":
                col = (x,"c")
                draw_win(col)

            #Pionowo
            elif symbol[x]+symbol[x+3]+symbol[x+6] == "xxx":
                row = ("r",x)
                draw_win(row)
            elif symbol[x]+symbol[x+3]+symbol[x+6] == "ooo":
                row = ("r",x)
                draw_win(row)

            #Skos
            elif symbol[0]+symbol[4]+symbol[8] == "xxx":
                diag = (2,2)
                draw_win(diag)
            elif symbol[2]+symbol[4]+symbol[6] == "xxx":
                diag = (3,3)
                draw_win(diag)
            elif symbol[0]+symbol[4]+symbol[8] == "ooo":
                diag = (2, 2)
                draw_win(diag)
            elif symbol[2]+symbol[4]+symbol[6] == "ooo":
                diag = (3, 3)
                draw_win(diag)


def main():
    game()

main()
