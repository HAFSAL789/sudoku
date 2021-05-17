import copy
import pygame
import time
import sudokualgo
import os

#general things
pygame.init()
gamescreen = pygame.display.set_mode((500, 530))
pygame.display.set_caption("sudoku")
icon_img = pygame.image.load(os.path.join("fonts","icon.png"))
pygame.display.set_icon(icon_img)

# secondary board for highlighting red color around the possible places where user can put numbers
board1 = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9],
         ]


# time function

def timefun(seconds):
    sec = seconds % 60
    min = seconds//60
    hour = min//60
    return str(int(hour))+":"+str(int(min))+":"+str(int(sec))


#to display won
def win():
    win_font = pygame.font.Font(os.path.join("fonts","starjedi.ttf"), 19)
    renderd_Win = win_font.render("won", True, (255, 191, 0))
    return gamescreen.blit(renderd_Win,(350,0)),gamescreen.blit(renderd_Win,(150,0))

#to display wrong
def failed():
    win_font = pygame.font.Font(os.path.join("fonts","starjedi.ttf"), 19)
    renderd_Win = win_font.render("Wrong", True, (255,0, 0))
    return gamescreen.blit(renderd_Win, (300, 0)), gamescreen.blit(renderd_Win, (150, 0))

#create a button
def buttonfun(color,size,border):
    return pygame.draw.rect(gamescreen,color,size,border)

# second screen
def sudokufun():
    start = time.time()
    gamescreen.fill((178, 190, 181))
    #fonts
    mainmenu = pygame.font.Font(os.path.join("fonts","MyUglyHandwriting-Regular.otf"),25)
    board_numbers = pygame.font.Font(os.path.join("fonts", "zector.ttf"), 30)


    # to keep looping until false
    running=True

    while running:
        # mouse positions
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # to store key value
        key = None

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

            # to get keys 1 to 9
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_1 or events.key == pygame.K_KP1:
                    key = 1
                elif events.key == pygame.K_2 or events.key == pygame.K_KP2:
                    key = 2
                elif events.key == pygame.K_3 or events.key == pygame.K_KP3:
                    key = 3
                elif events.key == pygame.K_4 or events.key == pygame.K_KP4:
                    key = 4
                elif events.key == pygame.K_5 or events.key == pygame.K_KP5:
                    key = 5
                elif events.key == pygame.K_6 or events.key == pygame.K_KP6:
                    key = 6
                elif events.key == pygame.K_7 or events.key == pygame.K_KP7:
                    key = 7
                elif events.key == pygame.K_8 or events.key == pygame.K_KP8:
                    key = 8
                elif events.key == pygame.K_9 or events.key == pygame.K_KP9:
                    key = 9

        for k in range(9):
            for i in range(9):

                # to find the grid where mousepointer is present
                # 55.5 is width and height of each grid

                if mouse_x in range(int(i * 55.5), int(i * 55.5 + 55.5)) and mouse_y in range(int(k * 55.5 + 30),
                                                                                              int(k * 55.5 + 30 + 55.5)) and \
                        board1[k][i] == 0:

                    # if key is pressed, it will pass to the board
                    if key!=None:
                        sudokualgo.board[k][i] = key

                    # to highlight the grid boders with red
                    buttonfun((255,0,0), (i * 55.5, k * 55.5 + 30, 55.5, 55.5), 1)

                else:

                    #to highlight the gird with white
                    buttonfun((255,255,255), (i * 55.5, k * 55.5 + 30, 55.5, 55.5), 0)

                    # to highlight grid borders
                    if mouse_x in range(int(i*55.5),int(i*55.5+55.5)) and mouse_y in range(int(k * 55.5+30),int(k*55.5+30+55.5)):
                        # with blue colour
                        buttonfun((0,0,255), (i * 55.5, k * 55.5 + 30, 55.5, 55.5), 1)

                    else:
                        # with some weird colour, i think its ash idk.
                        buttonfun((178, 190, 181), (i * 55.5, k * 55.5 + 30, 55.5, 55.5), 1)

                # to add numbers from board to screen
                if board1[k][i] == 0:
                    # in brown
                    digit = board_numbers.render(str(sudokualgo.board[k][i]), True, (111,67,33))

                else:
                    #in black
                    digit = board_numbers.render(str(sudokualgo.board[k][i]), True, (0, 0, 0))

                gamescreen.blit(digit, (i * 55.5 + 20, k * 55.5 + 30 + 20))


        # to draw black solid lines
        pygame.draw.line(gamescreen, (0, 0, 0), (166, 0), (166, 600), 1)
        pygame.draw.line(gamescreen, (0, 0, 0), (332, 0), (332, 600), 1)
        pygame.draw.line(gamescreen, (0, 0, 0), (0, 196.5), (600, 196.5), 1)
        pygame.draw.line(gamescreen, (0, 0, 0), (0, 362), (600, 362), 1)

        # board to display time,startagain ...
        buttonfun((255, 255, 255), (0, 0, 600, 30), 0)

        # manage clock
        timer = timefun(time.time()-start)
        timerfont = pygame.font.Font(os.path.join("fonts","MyUglyHandwriting-Regular.otf"), 25).render(timer,True,(0,0,0))
        gamescreen.blit(timerfont,(450,4))

        # solve button
        if mouse_x in range(250, 290) and mouse_y in range(5, 22):
            rendered_solve = mainmenu.render("solve", True, (178, 132, 190))
            # actually this should be inside a event loop but to save looping time i tried this way, it works somehow
            if events.type == pygame.MOUSEBUTTONDOWN:
                if events.button == 1:
                    sudokualgo.board = copy.deepcopy(board1)
                    sudokualgo.start()
                    sudokualgo.board = copy.deepcopy(sudokualgo.copyboard)
        else:
            rendered_solve = mainmenu.render("solve", True, (0, 0, 0))

        #mainmenu button
        if mouse_x in range(0, 72) and mouse_y in range(4, 23):
            rendered_start = mainmenu.render('mainmenu', True, (178, 132, 190))
            if events.type == pygame.MOUSEBUTTONDOWN:
                if events.button == 1:
                    sudokualgo.board = copy.deepcopy(board1)
                    return mainfun()
        else:
            rendered_start = mainmenu.render('mainmenu', True, (0, 0, 0))

        # to display both start and solve button
        gamescreen.blit(rendered_start,(0,0))
        gamescreen.blit(rendered_solve, (250, 0))
        
        # check whether user failed or not
        for solved in range(9):
            if 0 in sudokualgo.board[solved]:
                break
        else:
            if sudokualgo.check_user(sudokualgo.board) == "False":
                failed()
            else:
                win()

        # to thank pygame
        pygame.display.update()


# main function
def mainfun():

    #general things
    gamescreen.fill((255,109,58))
    font = pygame.font.Font(os.path.join("fonts","space age.ttf"),40)
    font_button = pygame.font.Font(os.path.join("fonts","starjedi.ttf"),35)
    text = font.render("sudoku",True,(255,255,255))

    # newgame button
    buttonfun((255, 255, 255), (150, 217, 200, 30), 0)
    text_button = font_button.render("newgame", True, (255, 0, 0))


    run = True
    while run:
        gamescreen.blit(text, (140, 150))
        gamescreen.blit(text_button, (160, 200))
        # again to thank pygame
        pygame.display.update()

        mouse_pos_X,mouse_pos_y = pygame.mouse.get_pos()
        # to quit
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

            # clicking newgame will start sudokufun
            if mouse_pos_X in range(150,350) and mouse_pos_y in range(217,247):
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if events.button == 1:
                        sudokufun()
                        run = False
                # button color red with white font
                buttonfun((255,0,0),(150,217,200,30),0)
                text_button = font_button.render("newgame", True, (255,255,255))
            else:
                # button color white with red font
                buttonfun((255, 255, 255), (150, 217, 200, 30), 0)
                text_button = font_button.render("newgame", True, (255, 0, 0))



mainfun()

# its my first python and pygame project,if u saw any mistakes pls inform