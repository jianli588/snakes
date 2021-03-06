import pygame
from pygame.locals import *

from Location import Snake, Food
from AI import Transverse
import Constants
# constants


WIN = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("Snake!")
pygame.event.pump()

snake = Snake()
food = Food()
ai = Transverse()


# https://stackoverflow.com/a/61007670
def draw_grid():
    for x in range(0, Constants.WIDTH, Constants.BLOCK_SIZE):
        for y in range(0, Constants.HEIGHT, Constants.BLOCK_SIZE):
            rect = pygame.Rect(x, y, Constants.BLOCK_SIZE, Constants.BLOCK_SIZE)
            pygame.draw.rect(WIN, Constants.GREEN, rect, 1)


def draw_window():
    snake.move()
    WIN.fill(Constants.BACKGROUND)

    # draw the body
    for segment in snake.segments[1:len(snake.segments)-1]:
        pygame.draw.rect(WIN, Constants.RED, pygame.Rect(Constants.BLOCK_SIZE*segment[0],
                                                         Constants.BLOCK_SIZE*segment[1],
                                                         Constants.BLOCK_SIZE,
                                                         Constants.BLOCK_SIZE))

    # draw the tail
    pygame.draw.rect(WIN, Constants.BLUE, pygame.Rect(Constants.BLOCK_SIZE * snake.segments[-1][0],
                                                     Constants.BLOCK_SIZE * snake.segments[-1][1],
                                                     Constants.BLOCK_SIZE,
                                                     Constants.BLOCK_SIZE))

    # draw the head
    head_rectangle = pygame.draw.rect(WIN, Constants.YELLOW, pygame.Rect(Constants.BLOCK_SIZE*snake.head[0],
                                                                      Constants.BLOCK_SIZE*snake.head[1],
                                                                      Constants.BLOCK_SIZE,
                                                                      Constants.BLOCK_SIZE))

    food_cord = [Constants.BLOCK_SIZE*food.coordinates[0], Constants.BLOCK_SIZE*food.coordinates[1]]
    food_rectangle = pygame.draw.circle(WIN, Constants.YELLOW, center=food_cord, radius=Constants.FOOD_RADIUS)

    draw_grid()

    if food_rectangle.colliderect(head_rectangle):
        food.refresh(snake)
        snake.extend()

    pygame.display.update()


def ai_play():

    next_move = ai.move(food.coordinates)

    if next_move == Constants.RIGHT:
        snake.turn_right()

    elif next_move == Constants.LEFT:
        snake.turn_left()

    elif next_move == Constants.UP:
        snake.turn_up()

    else:
        snake.turn_down()


def key_pressed():
    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        snake.turn_left()
    elif keys[K_RIGHT]:
        snake.turn_right()
    elif keys[K_DOWN]:
        snake.turn_down()
    elif keys[K_UP]:
        snake.turn_up()


def main():
    draw_window()

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(Constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ai_play()
        #key_pressed()
        draw_window()

        if snake.collision():
            run = False

    pygame.quit()
    print(f"points: {snake.point}")


if __name__ == '__main__':
    main()
