import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((32, 32))
        self.image.set_colorkey((1, 2, 3))
        self.image.fill((1, 2, 3))
        pygame.draw.rect(self.image, pygame.Color('dodgerblue'), (0, 0, 32, 32))
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.vel_y = 0
        self.on_ground = False

    def update(self):
        self.rect.y += self.vel_y
        if not self.on_ground:
            self.vel_y += 0.5
        self.on_ground = False

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, color, *grps):
        super().__init__(*grps)
        self.image = pygame.Surface((64, 16))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    colors = ['green', 'yellow', 'white', 'blue']

    platforms = pygame.sprite.Group()
    for _ in range(20):
        pos = random.randint(100, 700), random.randint(100, 600)
        Platform(pos, pygame.Color(random.choice(colors)), platforms)

    player = Player((400, 300))

    clock = pygame.time.Clock()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and player.on_ground:
                    player.vel_y = -10

        player.on_ground = False
        for platform in pygame.sprite.spritecollide(player, platforms, False):
            if player.vel_y > 0 and player.rect.bottom <= platform.rect.top + 10:
                player.rect.bottom = platform.rect.top
                player.vel_y = 0
                player.on_ground = True

        player.update()

        screen.fill((30, 30, 30))
        platforms.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
