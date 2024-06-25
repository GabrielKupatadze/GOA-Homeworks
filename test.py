import pygame
import sys
import random

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

SPEED = 60   
GRAVITY = 1
FLAP_STRENGTH = -10     
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
BIRD_WIDTH = 30
BIRD_HEIGHT = 30

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")

bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(BLUE)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = 600 // 2
        self.velocity = 0
        self.image = bird_image

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

class Pipe:
    def __init__(self, x, height, is_bottom):
        self.x = x
        self.height = height
        self.is_bottom = is_bottom

    def move(self):
        self.x -= 5

    def draw(self, screen):
        if self.is_bottom:
            pygame.draw.rect(screen, BLACK, (self.x, 600 - self.height, PIPE_WIDTH, self.height))
        else:
            pygame.draw.rect(screen, BLACK, (self.x, 0, PIPE_WIDTH, self.height))

    def get_rect(self):
        if self.is_bottom:
            return pygame.Rect(self.x, 600 - self.height, PIPE_WIDTH, self.height)
        else:
            return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)

def check_collision(bird, pipes):
    bird_rect = bird.get_rect()
    if bird.y < 0 or bird.y > 600 - BIRD_HEIGHT:
        return True
    for pipe in pipes:
        if bird_rect.colliderect(pipe.get_rect()):
            return True
    return False

def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []

    for i in range(2):
        height = random.randint(100, 600 - PIPE_GAP - 100)
        pipes.append(Pipe(400 + i * 200, height, False))
        pipes.append(Pipe(400 + i * 200, 400 - height - PIPE_GAP, True))

    score = 0
    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.move()

        for pipe in pipes:
            pipe.move()
            pipe.draw(screen)

        if check_collision(bird, pipes):
            running = False

        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)
            pipes.pop(0)
            height = random.randint(100, 600  - PIPE_GAP - 100)
            pipes.append(Pipe(400, height, False))
            pipes.append(Pipe(400, 600 - height - PIPE_GAP, True))
            score += 1

        bird.draw(screen)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()
