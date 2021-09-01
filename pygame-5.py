import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
image_sky_surface = pygame.image.load("graphics/Sky.png").convert()
image_ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface_font = pygame.font.Font("font/Pixeltype.ttf",50)
text_surface = text_surface_font.render('My game',False,(0,0,0)).convert()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
rectangle_snail = snail_surface.get_rect(bottomright = (600,300))
main_hero_surface =  pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
rectange_main_hero_surface = main_hero_surface.get_rect(midbottom=(80,300))
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    screen.blit(snail_surface,rectangle_snail)
    rectangle_snail.x -= 4
    if rectangle_snail.right <= 0:
        rectangle_snail.left = 800
    screen.blit(main_hero_surface,rectange_main_hero_surface)

    pygame.display.update()
    clock_object.tick(60)

