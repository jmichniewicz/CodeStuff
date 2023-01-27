import pygame

# Set up the pygame window and game loop
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

# Create a 2D array representing the level layout
level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Load Gene's sprite sheet and create an animation
gene_sprites = pygame.image.load("gene_sprites.png")
gene_animation = []
for i in range(3):
    gene_animation.append(gene_sprites.subsurface((i*32, 0, 32, 32)))
gene_index = 0

# Create a sprite for Gene and set his initial position
gene = pygame.sprite.Sprite()
gene.image = gene_animation[0]
gene.rect = gene.image.get_rect()
gene.rect.x = 32
gene.rect.y = 32

# Set Gene's initial velocity
gene.vx = 0
gene.vy = 0

# Set Gene's jumping speed and gravity
JUMP_SPEED = -8
GRAVITY = 0.5

# Set the size of each tile in the level
TILE_SIZE = 32

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gene.vx = -5
            elif event.key == pygame.K_RIGHT:
                gene.vx = 5
            elif event.key == pygame.K_UP:
                gene.vy = JUMP_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                gene.vx = 0

    # Update Gene's position and velocity
   
