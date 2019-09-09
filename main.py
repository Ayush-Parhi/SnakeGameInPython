import pygame
import random
import os

pygame.mixer.init()

pygame.init()
screen = pygame.display.set_mode((1200, 900))
# colors
white = (255, 255, 255)
red = (255,  0, 0)
black = (0, 0, 0)
green = (130, 170, 0)
# creating window
screen_width = 850
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg1 = pygame.image.load("intro.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.image.load("last.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes By Ayush")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])


def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# Welcome Screen


def welcome():

    exit_game = False
    while not exit_game:
        game_window.fill((233, 210, 229))
        game_window.blit(bgimg1, (0,0))
        text_screen("WELCOME TO SNAKES!!", black, 290, 250)
        text_screen("Created by Ayush", black, 320, 290)
        text_screen("Press Enter to play", black, 315, 330)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()


        pygame.display.update()
        clock.tick(60)

# Game Loop


def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    highscore = 0

    # check if high score file exists
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    snake_size = 9
    init_velocity = 5
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            game_window.fill(green)
            game_window.blit(bgimg2, (0, 0))
            text_screen("GAME OVER!! ", red, 390, 210)
            text_screen("Score : " + str(score), red, 390, 230)
            text_screen("Press enter to continue.", red, 390, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = - init_velocity

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                        # CHEAT CODES:

                    if event.key == pygame.K_s:
                        init_velocity -= 1

                    if event.key == pygame.K_k:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                pygame.mixer.music.load('point.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(20, 800)
                food_y = random.randint(20, 550)
                snk_length += 5
                if score > int(highscore):
                    highscore = score
            game_window.fill(green)
           # gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(game_window, black, snk_list , snake_size )
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()






