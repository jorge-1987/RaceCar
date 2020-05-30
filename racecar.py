import pygame
import time
import random
from assets.constants import (
    SCREEN_RESOLUTION,
    WHITE,
    BLACK,
    BGREEN,
    GREEN,
    GREY,
    DARKGREY,
    RED,
    BRED,
    PLAYER_IMAGE_PATH,
    ENEMY_IMAGE_PATH
)
from assets.controls import draw_text, Basic_button, Basic_car, Basic_grass

pygame.init()


dodged = 0

screen = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption('Car Dodger')
clock = pygame.time.Clock()


def quitgame():
    pygame.quit()
    quit()

def crash():
    draw_text(screen,
              "You crashed!",
              115,
              BLACK,
              SCREEN_RESOLUTION[0]/2,
              SCREEN_RESOLUTION[1]/2
              )

    pygame.display.update()


def game_intro():
  # Init
    intro = True
    buttons = [
        Basic_button(
            "Start!",
            (150, 450),
            (100, 50),
            GREEN,
            BGREEN,
            game_loop
        ),
        Basic_button(
            "Exit",
            (550, 450),
            (100, 50),
            RED,
            BRED,
            quitgame
        )
    ]

    # Intro Loop
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Clear screen
        screen.fill(WHITE)

        # Actions
        click = pygame.mouse.get_pressed()
        if click[0]:
            for button in buttons:
                button.do_action()

        # Draw
        player.draw_score(screen)

        draw_text(screen,
                  "Race Car",
                  115,
                  BLACK,
                  SCREEN_RESOLUTION[0]/2,
                  SCREEN_RESOLUTION[1]/2
                  )
        for button in buttons:
            button.draw(screen)

        pygame.display.update()


def game_loop():
  # Generate random Enemy
    enemy = Basic_car(
        [random.randrange(150, (SCREEN_RESOLUTION[0]-232)), 0],
        [82, 82],
        [0, 7],
        pygame.image.load(ENEMY_IMAGE_PATH)
    )

    # MAP
    left_grass = Basic_grass([0, 0], [130, SCREEN_RESOLUTION[1]], GREEN)
    left_curve = Basic_grass([130, 0], [20, SCREEN_RESOLUTION[1]], DARKGREY)

    right_curve = Basic_grass(
        [(SCREEN_RESOLUTION[0]-150), 0], [20, SCREEN_RESOLUTION[1]], DARKGREY)
    right_grass = Basic_grass(
        [(SCREEN_RESOLUTION[0]-130), 0], [130, SCREEN_RESOLUTION[1]], GREEN)


# LOOP PRINCIPAL DEL JUEGO
    looping = True
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            player.speed = [0, 0]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed[0] = - 5
                if event.key == pygame.K_RIGHT:
                    player.speed[0] = 5

        # Move
        player.move()
        enemy.move()
        if (enemy.pos[1] > SCREEN_RESOLUTION[1]):
            player.score += 1
            enemy.pos[1] = - enemy.size[1]
            enemy.pos[0] = random.randrange(150, (SCREEN_RESOLUTION[0]-232))

        # Collisions
        looping = looping * player.collision(enemy)
        looping = looping * player.collision(left_curve)
        looping = looping * player.collision(right_curve)

        # Draw
        screen.fill(GREY)

        # Draw Map
        left_grass.draw(screen)
        left_curve.draw(screen)
        right_curve.draw(screen)
        right_grass.draw(screen)

        # DRAW
        player.draw(screen)
        enemy.draw(screen)

        player.draw_score(screen)

        pygame.display.update()
        clock.tick(60)

    crash()
    time.sleep(2)
    player.pos = [SCREEN_RESOLUTION[0] * 0.45, SCREEN_RESOLUTION[1] * 0.8]


if __name__ == "__main__":
    player = Basic_car(
        [SCREEN_RESOLUTION[0] * 0.45, SCREEN_RESOLUTION[1] * 0.8],
        [82, 82],
        [0, 0],
        pygame.image.load(PLAYER_IMAGE_PATH)
    )
    loop = True

    while loop:
        game_intro()
