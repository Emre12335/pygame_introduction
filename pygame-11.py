import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# Fonts for text surfaces
my_game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
# Surfaces/PlayScreen
sky_s = pygame.image.load("graphics/Sky.png").convert()
ground_s = pygame.image.load("graphics/ground.png").convert()
snail_s = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
player_s = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
my_game_s = my_game_font.render("My Game", False, (64, 64, 64)).convert()

# Rectangles/PlayScreen
snail_r = snail_s.get_rect(bottomleft=(800, 300))
player_r = player_s.get_rect(midbottom=(100, 300))
my_game_r = my_game_s.get_rect(midtop=(400, 10))

# Variables
snail_left = -4
gravity = 0
game_play = True
# score variables
score = 0
old_score = 0
# score surface-rectangles
score_s = my_game_font.render(f"{score}",False,(64,64,64))
score_r = score_s.get_rect(midbottom = (400,400))


# Game off
player_s_menu = pygame.transform.scale2x(player_s).convert_alpha()
player_s_menu_r = player_s_menu.get_rect(center=(400, 200))
font_1 = pygame.font.Font("font/Pixeltype.ttf", 35)
font_2 = pygame.font.Font("font/Pixeltype.ttf", 60)
pixelspace = font_1.render("Press space to start the game", False, (111, 196, 169)).convert()
pixel = font_2.render("PixelRunner", False, (111, 196, 169)).convert()
pixel_r = pixel.get_rect(midbottom=(player_s_menu_r.centerx + 5, player_s_menu_r.top - 20))
pixelspace_r = pixelspace.get_rect(center=(player_s_menu_r.centerx, player_s_menu_r.bottom + 35))

while True:

    # Event area
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_play:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_r.bottom >= 300:
                    gravity = - 25
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_r.collidepoint(event.pos):
                    gravity = - 25
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_play = True
                    snail_r.left = 800
                    old_score = pygame.time.get_ticks()
                    # altta yazan sebebin aynısı bura için de geçerli.
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_play = True
                snail_r.left = 800
                old_score = pygame.time.get_ticks() # old score u buraya bu şekilde yazmamızın sebebi
                # bu buraya kaydedildikten sonra yenilenmeyecek olması yani score hep sabit kalacak
                # sadece oyun durup yeniden başladığında güncellenecek.
    if snail_r.colliderect(player_r):
        game_play = False

    # Game on
    if game_play:
        # Blit area
        screen.blit(sky_s, (0, 0))
        screen.blit(ground_s, (0, 300))
        screen.blit(my_game_s, my_game_r)
        screen.blit(player_s, player_r)
        screen.blit(snail_s, snail_r)
        screen.blit(score_s,score_r)

        # Draw
        pygame.draw.rect(screen, "#c0e8ec", my_game_r, 16, 6)
        screen.blit(my_game_s, my_game_r)

        # Move snail
        snail_r.x += snail_left
        if snail_r.right <= 0:
            snail_r.left = 800
        # Gravity
        gravity += 1
        player_r.y += gravity
        if player_r.bottom > 300:
            player_r.bottom = 300
        # Score board update
        score = pygame.time.get_ticks() - old_score
        score_s = my_game_font.render(f"{score//1000}",False,(64,64,64)).convert()

    # Game off
    else:
        # score u birebir alıp yansıtıyoruz.çünkü if player_active in içinde olduğu için
        # yenilenmiyor.Ve sabit olarak kalıyor.
        score_s2 = my_game_font.render(f"score:{score//1000}",False,(64,64,64)).convert()
        score_s2_r = score_s2.get_rect(center = (pixelspace_r.centerx,pixelspace_r.bottom + 25))
        # Blit
        screen.fill((94, 129, 162))
        screen.blit(player_s_menu, player_s_menu_r)
        screen.blit(pixel, pixel_r)
        screen.blit(pixelspace, pixelspace_r)
        screen.blit(score_s2,score_s2_r)

    # Display and Clock
    clock.tick(60)
    pygame.display.update()
