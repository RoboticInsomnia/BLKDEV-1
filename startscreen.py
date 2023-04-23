import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Game settings
clock = pygame.time.Clock()

# Start screen
def start_screen():
    font = pygame.font.Font(None, 64)
    title_text = font.render("My Game", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen_width/2, screen_height/4))

    font = pygame.font.Font(None, 32)
    start_text = font.render("Press SPACE to start", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2))

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        # Draw the start screen
        screen.fill((0, 0, 0)) # black background
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)

        # Update the screen
        pygame.display.flip()
        clock.tick(60)

# Start the game
start_screen()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Draw game elements
    screen.fill((255, 255, 255)) # white background

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()