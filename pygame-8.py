# Yer çekimi ve zemin yaratma pygame
# Yer çekimi yaratmak için önce player gravity variable ını oluşturduk Bu variable # 1
# her while loop döndüğünde 1 artacak şekilde yazdık player_gravity += 1 Bu sayede oyuncu zemine doğru çekilerek # 2
# gözden kayboluyor. Ardından tuş ayarını space e basıldığı zaman gravity i -20 yapcak şekilde ayarlıyoruz. Bu sayede# 3
# tuşa basıldığında += 1 den dolayı azalarak yukarı sıçrıyor gibi gözüküyor. ardından değer yine pozitif olunca yere
# doğru hareket ediyor. Zemin oluşturmak için ise eğer hero_r.bottom >= 300 ise hero_r.bottom = 300 yazarak zemin # 4
# oluşturuyoruz. bunların hepsini hero_r blit işlemi gerçekleşmeden yapıyoruz bu sayede  while loop döndükçe hareket
# ediyor gibi gözüküyor.
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
player_gravity = 0 # 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: # 3
            if event.key == pygame.K_SPACE and hero_r.bottom >= 300: # 3
                player_gravity = -20 # 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hero_r.collidepoint(event.pos) and hero_r.bottom >= 300:
                player_gravity = -20
    screen.blit(sky_s, (0, 0))
    screen.blit(ground_s, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_r)
    pygame.draw.rect(screen, "#c0e8ec", text_r, 8)
    screen.blit(text_s, text_r)
    # Hero blit
    player_gravity += 1 # 2
    hero_r.y += player_gravity
    if hero_r.bottom >= 300: # 4
        hero_r.bottom = 300 # 4
    screen.blit(hero_s, hero_r) # bu işlemleri blit gerçekleşmeden yapıyoruz ki while loop döndükçe çalışmaya devam
    # etsin.
    screen.blit(snail_s, snail_r)
    snail_r.x -= 4
    if snail_r.right <= 0:
        snail_r.left = 800
    pygame.display.update()
    clock.tick(60)

