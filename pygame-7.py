import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
# surfaces
ground_s = pygame.image.load("graphics/ground.png").convert()
sky_s = pygame.image.load("graphics/Sky.png").convert()
snail_s = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
hero_s = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
# text surface
font = pygame.font.Font("font/Pixeltype.ttf", 50)
text_s = font.render("My game", False, (64, 64, 64)).convert()
# rectangles
snail_r = snail_s.get_rect(bottomleft=(800, 300))
hero_r = hero_s.get_rect(bottomleft=(50, 300))
text_r = text_s.get_rect(midtop=(400, 35))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:#for loop da ise önce basılıp basılmadığını kontrol etmemiz gerekiyor.
            print("pressed")
        if event .type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("space")
    screen.blit(sky_s, (0, 0))
    screen.blit(ground_s, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_r)
    pygame.draw.rect(screen, "#c0e8ec", text_r, 8)
    screen.blit(text_s, text_r)
    screen.blit(hero_s, hero_r)
    screen.blit(snail_s, snail_r)
    snail_r.x -= 4
    if snail_r.right <= 0:
        snail_r.left = 800
    keys = pygame.key.get_pressed() # önce keys in yer aldığı bir dictonary yazıyoruz.
    if keys[pygame.K_SPACE]: # dictonary i kontrol edioyruz.
        print("jump") # bu birinci yol
    pygame.display.update()
    clock.tick(60)
