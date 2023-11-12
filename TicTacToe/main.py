import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
pos_x = WIDTH / 4
pos_y = (0.1 * HEIGHT)
rec_width = WIDTH - 0.5 * WIDTH
rec_height = HEIGHT - 0.2 * HEIGHT
sector_width = rec_width/3
sector_height = rec_height/3

black = (0, 0, 0)
white = (255, 255, 255)
other = (211,30,24)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clicked = [0,0,0,0,0,0,0,0,0]
symbol = [0,0,0,0,0,0,0,0,0]

line1_list = [[(pos_x, pos_y), (pos_x+sector_width, pos_y+sector_height)], [(pos_x+sector_width, pos_y), (pos_x+sector_width*2, pos_y+sector_height)], [(pos_x+sector_width*2, pos_y), (pos_x+sector_width*3, pos_y+sector_height)],
              [(pos_x, pos_y+sector_height), (pos_x+sector_width, pos_y+sector_height*2)], [(pos_x+sector_width, pos_y+sector_height), (pos_x+sector_width*2, pos_y+sector_height*2)], [(pos_x+sector_width*2, pos_y+sector_height), (pos_x+sector_width*3, pos_y+sector_height*2)],
              [(pos_x, pos_y+sector_height*2), (pos_x+sector_width, pos_y+sector_height*3)], [(pos_x+sector_width, pos_y+sector_height*2), (pos_x+sector_width*2, pos_y+sector_height*3)], [(pos_x+sector_width*2, pos_y+sector_height*2), (pos_x+sector_width*3, pos_y+sector_height*3)]]

line2_list =  [[(pos_x, pos_y+sector_height), (pos_x+sector_width, pos_y)], [(pos_x+sector_width, pos_y+sector_height), (pos_x+sector_width*2, pos_y)], [(pos_x+sector_width*2, pos_y+sector_height), (pos_x+sector_width*3, pos_y)],
               [(pos_x, pos_y+sector_height*2), (pos_x+sector_width, pos_y+sector_height)], [(pos_x+sector_width, pos_y+sector_height*2), (pos_x+sector_width*2, pos_y+sector_height)], [(pos_x+sector_width*2, pos_y+sector_height*2), (pos_x+sector_width*3, pos_y+sector_height)],
               [(pos_x, pos_y+sector_height*3), (pos_x+sector_width, pos_y+sector_height*2)], [(pos_x+sector_width, pos_y+sector_height*3), (pos_x+sector_width*2, pos_y+sector_height*2)], [(pos_x+sector_width*2, pos_y+sector_height*3), (pos_x+sector_width*3, pos_y+sector_height*2)]]


circle_list =  [(pos_x+sector_width/2, pos_y+sector_height/2), (pos_x+sector_width/2*3, pos_y+sector_height/2), (pos_x+sector_width/2*5, pos_y+sector_height/2),
                (pos_x+sector_width/2, pos_y+sector_height/2*3), (pos_x+sector_width/2*3, pos_y+sector_height/2*3), (pos_x+sector_width/2*5, pos_y+sector_height/2*3),
                (pos_x+sector_width/2, pos_y+sector_height/2*5), (pos_x+sector_width/2*3, pos_y+sector_height/2*5), (pos_x+sector_width/2*5, pos_y+sector_height/2*5)]

mouse_range = line1_list[:]

state = False




# position > (300, 80) and position < (500, 293) and clicked[0] == False:

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

    # # Pozycja 2
    # if position > mouse_range[1][0] and position < mouse_range[1][1] and clicked[1] == False:
    #     if pygame.mouse.get_pressed()[0] == True:
    #         clicked[1] = True
    #         if state == False:
    #             symbol[1] = "x"
    #         elif state == True:
    #             symbol[1] = "o"
    #         state = not state
    #
    # # Pozycja 3
    # if position > (700, 80) and position < (900, 293) and clicked[2] == False:
    #     if pygame.mouse.get_pressed()[0] == True:
    #         clicked[2] = True
    #         if state == False:
    #             symbol[2] = "x"
    #         elif state == True:
    #             symbol[2] = "o"
    #         state = not state











def draw_symbols():

    for i in range(9):
        if clicked[i] == True and symbol[i] == "x":
            pygame.draw.lines(screen, white, True, line1_list[i], 5)
            pygame.draw.lines(screen, white, True, line2_list[i], 5)
        elif clicked[i] == True and symbol[i] == "o":
            pygame.draw.circle(screen, white, circle_list[i], 100, 4)

        # # Pole 2
        # if clicked[1] == True and symbol[1] == "x":
        #     pygame.draw.lines(screen, white, True, line1_list[1], 5)
        #     pygame.draw.lines(screen, white, True, line2_list[1], 5)
        # elif clicked[1] == True and symbol[1] == "o":
        #     pygame.draw.circle(screen, white, circle_list[1], 100, 4)
        #
        # # Pole 3
        # if clicked[2] == True and symbol[2] == "x":
        #     pygame.draw.lines(screen, white, True, line1_list[2], 5)
        #     pygame.draw.lines(screen, white, True, line2_list[2], 5)
        # elif clicked[2] == True and symbol[2] == "o":
        #     pygame.draw.circle(screen, white, circle_list[2], 100, 4)
        # ... i tak dalej bym musiał wypisywać





# def draw_symbols_o():
#         mouse_click()
#         if clicked[0] == True:
#             pygame.draw.circle(screen, white, (400, 187), 100, 4)


        # print(position)


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
        mouse_click()
        draw_symbols()
        pygame.display.flip()
        clock.tick(60)
        print(pygame.mouse.get_pos())
    pygame.quit()

#def rules():


def main():
    game()

main()
