import pygame

# Initialize Pygame
pygame.init()

# Set up screen parameters
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

# Set background color
background_color = (58, 58, 58)

# Load and scale the image
image = pygame.image.load("penguin.png")  
image = pygame.transform.scale(image, (300, 300))

# Get rect of the image and center it
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    screen.blit(image, image_rect)
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()

