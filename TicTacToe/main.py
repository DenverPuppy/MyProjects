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


points1 = 0
points2 = 0


def get_turn():
    turn = random.randint(1, 10)
    if turn >= 5:
        temp_state = False
    else:
        temp_state = True
    return temp_state

state = get_turn()
round_end = False

def highlits():
    if state == False:
        pygame.draw.lines(screen, white, True, ((pos_x/4,pos_y+60), (pos_x/4+138,pos_y+60)), 5)
    elif state == True:
        pygame.draw.lines(screen, white, True, ((pos_x*3 + pos_x/4,pos_y+60),(pos_x*3 + pos_x/4 + 138,pos_y+60)), 5)

def player_text():
    global points1
    global points2
    points1_str = str(points1)
    points2_str = str(points2)
    text_font = pygame.font.SysFont("Impact", 40)
    score_font = pygame.font.SysFont("Impact", 120)

    score1 = score_font.render(points1_str, True, white)
    score2 = score_font.render(points2_str, True, white)

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
    if round_end == False:
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


def tie():
    tie_list = []
    for sym in symbol:
        if sym != "":
            tie_list.append("Tie")
        else:
            return
    tie_bool = all(i == tie_list[0] for i in tie_list)
    if tie_bool == True:
        winner = "none"
        new_game(winner)

def restart(winner):
    global state
    global clicked
    global symbol
    global round_end
    global points1
    global points2

    clicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    symbol = ["", "", "", "", "", "", "", "", ""]
    round_end = False
    if winner == "x":
        points1 += 1
        state = True
    elif winner == "o":
        points2 += 1
        state = False
    elif winner == "none":
        points1 = points1
        points2 = points2
        state = get_turn()




def new_game(winner):
    global round_end
    round_end = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] == True:
        restart(winner)
    else:
        pygame.draw.rect(screen, black, (WIDTH/5, HEIGHT/4, WIDTH*0.6 ,HEIGHT*0.4))
        pygame.draw.rect(screen, white, (WIDTH/5, HEIGHT/4, WIDTH*0.6 ,HEIGHT*0.4), width=5)
        text_font = pygame.font.SysFont("Impact", 65)
        text_font2 = pygame.font.SysFont("Impact", 45)
        if winner == "x":
            info = text_font.render("Player 1 won this round", True, white)
            info2 = text_font2.render("Press SPACE to play again", True, white)
            info3 =  text_font2.render("Press Q to Quit", True, white)
            screen.blit(info, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/20))
            screen.blit(info2, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/6))
            screen.blit(info3, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/4))

        elif winner == "o":
            info = text_font.render("Player 2 won this round", True, white)
            info2 = text_font2.render("Press SPACE to play again", True, white)
            info3 =  text_font2.render("Press Q to Quit", True, white)
            screen.blit(info, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/20))
            screen.blit(info2, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/6))
            screen.blit(info3, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/4))
        elif winner == "none":
            info = text_font.render("Tie !", True, white)
            info2 = text_font2.render("Press SPACE to play again", True, white)
            info3 =  text_font2.render("Press Q to Quit", True, white)
            screen.blit(info, (WIDTH/5+WIDTH/4,HEIGHT/4+HEIGHT/20))
            screen.blit(info2, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/6))
            screen.blit(info3, (WIDTH/5+WIDTH/20,HEIGHT/4+HEIGHT/4))

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
            print(event)
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
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
    print(symbol)
    for x in range(3):

        #Pionowo
        if symbol[x]+symbol[x+3]+symbol[x+6] == "xxx":
            row = ("r",x)
            draw_win(row)
            winner = "x"
            new_game(winner)
            return
        elif symbol[x]+symbol[x+3]+symbol[x+6] == "ooo":
            row = ("r",x)
            draw_win(row)
            winner = "o"
            new_game(winner)
            return

        #Poziomo
        elif symbol[x*3]+symbol[x*3+1]+symbol[x*3+2] == "xxx":
            col = (x,"c")
            draw_win(col)
            winner = "x"
            new_game(winner)
            return
        elif symbol[x*3]+symbol[x*3+1]+symbol[x*3+2] == "ooo":
            col = (x,"c")
            draw_win(col)
            winner = "o"
            new_game(winner)
            return

        #Skos
        elif symbol[0]+symbol[4]+symbol[8] == "xxx":
            diag = (2,2)
            draw_win(diag)
            winner = "x"
            new_game(winner)
            return

        elif symbol[2]+symbol[4]+symbol[6] == "xxx":
            diag = (3,3)
            draw_win(diag)
            winner = "x"
            new_game(winner)
            return

        elif symbol[0]+symbol[4]+symbol[8] == "ooo":
            diag = (2, 2)
            draw_win(diag)
            winner = "o"
            new_game(winner)
            return

        elif symbol[2]+symbol[4]+symbol[6] == "ooo":
            diag = (3, 3)
            draw_win(diag)
            winner = "o"
            new_game(winner)
            return

        elif x == 2:
            tie()



def main():
    game()

main()