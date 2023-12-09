import pygame
import sys
import random

# инициализация pygame
pygame.init()

# настройки фона
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (20, 30, 20)
STAR_COLOR = (255, 255, 255)
STAR_SIZE = 15
SPACESHIP_SPEED = 15
FALL_SPEED = 5
MAX_LIVES = 3
counter = 0

# создание окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Stars Game")

# создание корзинки
spaceship = pygame.image.load("basket.png")
spaceship = pygame.transform.scale(spaceship, (50, 50))
spaceship_position = [WIDTH // 2, HEIGHT - 70]

# создание списка яиц
stars = []

def create_star():
    x = random.randint(0, WIDTH - STAR_SIZE)
    y = random.randint(-STAR_SIZE, 0)
    return [x, y]

# таймер на генерацию яиц в миллисекундах
pygame.time.set_timer(pygame.USEREVENT, 1500)


lives = MAX_LIVES
clock = pygame.time.Clock()

# главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            # добавление нового яйца в список
            stars.append(create_star())

    # Move stars down
    for star in stars:
        star[1] += FALL_SPEED
        if star[1] > HEIGHT:
            lives -= 1
            stars.remove(star)

    # контроль корзинки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_position[0] > 0:
        spaceship_position[0] -= SPACESHIP_SPEED
    if keys[pygame.K_RIGHT] and spaceship_position[0] < WIDTH - 50:
        spaceship_position[0] += SPACESHIP_SPEED

    # проверка собранных яиц
    for star in stars:
        if (
            spaceship_position[0] < star[0] < spaceship_position[0] + 50
            and spaceship_position[1] < star[1] < spaceship_position[1] + 50
        ):
            stars.remove(star)
            counter = counter + 1

    # отрисовка
    window.fill(BACKGROUND_COLOR)
    for star in stars:
        pygame.draw.circle(window, STAR_COLOR, (star[0], int(star[1])), STAR_SIZE // 2)
    window.blit(spaceship, spaceship_position)

    # жизни
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    window.blit(lives_text, (10, 10))

    # счет
    font = pygame.font.Font(None, 36)
    counter_text = font.render(f"Counter: {counter}", True, (255, 255, 255))
    window.blit(counter_text, (10, 40))

    # проверка на конец игры
    if lives <= 0:
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 10, 10))
        window.blit(game_over_text, (WIDTH // 3, HEIGHT // 2.5))
        pygame.time.delay(200)
       

    # обновление экрана
    pygame.display.flip()
    clock.tick(30)  
