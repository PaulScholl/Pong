import pygame
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
width = 800
height = 600

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Velocidad de la pelota
ball_speed_x = 7
ball_speed_y = 7

# Velocidad de las palas
paddle_speed = 10

# Creación de la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ping Pong')

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Paletas y pelota
paddle_width = 10
paddle_height = 100
ball_size = 20

player1_paddle = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(width - 20, height // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Puntuación
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de las palas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s] and player1_paddle.bottom < height:
        player1_paddle.y += paddle_speed
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_paddle.bottom < height:
        player2_paddle.y += paddle_speed

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones con la parte superior e inferior
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y = -ball_speed_y

    # Colisiones con las paletas
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x = -ball_speed_x

    # Gol en la portería del jugador 2
    if ball.left <= 0:
        player2_score += 1
        ball.x, ball.y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x *= -1

    # Gol en la portería del jugador 1
    if ball.right >= width:
        player1_score += 1
        ball.x, ball.y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x *= -1

    # Dibujar en la pantalla
    screen.fill(black)
    pygame.draw.rect(screen, white, player1_paddle)
    pygame.draw.rect(screen, white, player2_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    # Mostrar puntuación
    player1_text = font.render(str(player1_score), True, white)
    screen.blit(player1_text, (width // 4, 20))

    player2_text = font.render(str(player2_score), True, white)
    screen.blit(player2_text, (width * 3 // 4, 20))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)