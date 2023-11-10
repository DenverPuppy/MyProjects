import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
black = (0, 0, 0)
white = (255, 255, 255)
other = (211,30,24)
screen = pygame.display.set_mode([WIDTH, HEIGHT])



def mouse_position():
    position = pygame.mouse.get_pos()
    print(position)
def draw_board():
    pos_x = WIDTH / 4
    pos_y = (0.1 * HEIGHT)
    rec_width = WIDTH - 0.5 * WIDTH
    rec_height = HEIGHT - 0.2 * HEIGHT

    pygame.draw.rect(screen, white, (pos_x, pos_y, rec_width, rec_height), width=5)
    for x in range(3):
        for y in range(3):
            pygame.draw.rect(screen, white, (pos_x+rec_width/3*x, pos_y+rec_height/3*y,rec_width/3,rec_height/3 ), width=1)
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
        mouse_position()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

#def rules():


def main():
    game()

main()
