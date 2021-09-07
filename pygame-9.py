# Score board ekleme
# score board eklemek için pygame.time.get_tick() i kullanacağız.
# pygame.time.get_ticks() pygame.init kurulduktan itibaren geçen süreyi gösterir
# değişken değildir(mutable) değildir 1 kere tanımlanınca değeri sabit kalır.
# fakat while loop un içine yazdığımız zaman yada oyunu birden fazla kez çalıştırınca
# farklı değerler ürettiğini görebiliriz.Bunun sebebi pygame.initten itibaren geçen süre
# her defasında değişecekdir.milisaniyeyi takip etmesi zor olduğu için bazen 762 bazen başka bir değer
# görülebilir.while loop un içinde ise değer sürekli olarak yenileneceği için büyüyerek gözükür.
# fakat normalde pygame.time.get_ticks statik ve değişmeyen bir değer oluşturur.
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
# variables
player_gravity = 0
while True:
    # loop variable for score
    score = pygame.time.get_ticks()
    # loop surface for score
    score_surface = font.render(f"{score//100}",False,(64,64,64))
    # loop rectangle of loop surface
    score_s_rec = score_surface.get_rect(midbottom = (400,400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hero_r.bottom >= 300:
                player_gravity = -20
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hero_r.collidepoint(event.pos) and hero_r.bottom >= 300:
                player_gravity = -20
    screen.blit(sky_s, (0, 0))
    screen.blit(ground_s, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_r)
    pygame.draw.rect(screen, "#c0e8ec", text_r, 8)
    screen.blit(text_s, text_r)
    # Hero blit
    player_gravity += 1
    hero_r.y += player_gravity
    if hero_r.bottom >= 300:
        hero_r.bottom = 300
    screen.blit(hero_s, hero_r)
    screen.blit(snail_s, snail_r)
    snail_r.x -= 4
    if snail_r.right <= 0:
        snail_r.left = 800
    # bliting the text
    screen.blit(score_surface,score_s_rec)
    pygame.display.update()
    clock.tick(60)
