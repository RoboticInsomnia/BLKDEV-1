import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BLKDEV.1")

# Game settings
clock = pygame.time.Clock()

# Game objects
player_image = pygame.image.load("assets/ori.png") # replace with your own image
player_rect = player_image.get_rect()
player_rect.center = (screen_width/2, screen_height/2)
player_speed = 5


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    elif keys[pygame.K_UP]:
        player_rect.y -= player_speed
    elif keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Draw game elements
    screen.fill((0, 0, 0)) # white background
    screen.blit(player_image, player_rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()