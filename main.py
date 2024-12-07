import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE, RED, BLUE, BLACK = (255, 255, 255), (255, 0, 0), (0, 0, 255), (0, 0, 0)
FPS = 60

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Initialize game objects
def init_game():
    paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
    ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2, 20, 20)
    bricks = [pygame.Rect(5 + i * 80, 5 + j * 30, 70, 20) for j in range(6) for i in range(10)]
    return paddle, ball, [4, -4], bricks, 3, 0

# Draw everything
def draw(paddle, ball, bricks, score, lives):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, WHITE), (WIDTH - 100, 10))
    pygame.display.flip()

# Main game loop
def main():
    paddle, ball, ball_speed, bricks, lives, score = init_game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-7, 0)
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.move_ip(7, 0)

        ball.move_ip(*ball_speed)
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] *= -1
        if ball.top <= 0:
            ball_speed[1] *= -1
        if ball.colliderect(paddle):
            ball_speed[1] *= -1
        if ball.bottom >= HEIGHT:
            lives -= 1
            ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2, 20, 20)
            if lives == 0:
                running = False

        hit_index = ball.collidelist(bricks)
        if hit_index != -1:
            ball_speed[1] *= -1
            bricks.pop(hit_index)
            score += 10

        draw(paddle, ball, bricks, score, lives)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()