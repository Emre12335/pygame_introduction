# rectanglelar ile çizim boyama yapma
# hazır kodda font u rectangle ile yerleştirdik ve pygame-5 deki collisionları attık.
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
ground_surface = pygame.image.load("graphics/ground.png").convert()
sky_surface = pygame.image.load("graphics/Sky.png").convert()
font_type = pygame.font.Font("font/Pixeltype.ttf", 50)
text_surface = font_type.render("My Game", False, (0, 0, 0)).convert()
text_rect  = text_surface.get_rect(midtop = (400,0))
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
hero_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomleft=(800, 300))
hero_rectangle = hero_surface.get_rect(midbottom=(100, 300))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,text_rect)
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(hero_surface, hero_rectangle)
    snail_rectangle.x -= 4
    if snail_rectangle.right == 0:
        snail_rectangle.left = 800
    clock.tick(60)
    pygame.display.update()
