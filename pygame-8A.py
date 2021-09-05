# Oyuncu tuşa basılıyken sağa sola hareket ettirme.
# For loop event ile key.get_pressed farkı.Hangisini ne zaman kullanmalıyız.
# For event in pygame.event.get_event() i kullandığımız KEYDOWN ve KEYUP tuşa basılı tutulduğu zaman algılanmıyor.
# Bu yüzden sağa sola hareket ettirmek için tercihimiz event loop oluyor.Fakat spacce tuşu için ise basılı tutulduğu
# zaman algılanmasını istemiyoruz bu tüzden sağa sola için pygame.ket.get_pressed() i  kullanırken diğeri için ise
# for loop u kullandık.player_gravity de olduğu gibi yine variable yaprarak gideceğiz.
# player_left ve player_right yaptıktan #1
# sonra loop döndüğünde aynı kalmaması için loop un içine de bir tane koyacağız. #2
# ardından tuşa basılıyken player_right ve player_left i 4 olarak ayarlayacağız. #3
# ve son olarak snail e yaptığımız şeyin aynısını yapacağız.eğer hero_r.left > 800 hero_r.right = 0 #4
# ve hero_r.right < 0 hero_r.left = 800 #Burda büyük eşit veya küçük eşit yazmamız lazım yoksa oyuncu arada sıkışıyor.#4
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
player_gravity = 0  # player_gravity
player_right = 0 # 1
player_left = 0 # 1
while True:
    player_right = 0 # 2
    player_left = 0 # 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
    keys = pygame.key.get_pressed() # 3
    if keys[pygame.K_RIGHT]: # 3
        player_right = 4 # 3
    if keys[pygame.K_LEFT]: # 3
        player_left = -4 # 3
    screen.blit(sky_s, (0, 0))
    screen.blit(ground_s, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_r)
    pygame.draw.rect(screen, "#c0e8ec", text_r, 8)
    screen.blit(text_s, text_r)
    # Hero blit
    hero_r.x += player_right # 2
    hero_r.x += player_left # 2
    player_gravity += 1  # playera gravity değeri verdik
    if hero_r.left > 800: # 4
        hero_r.right = 0 # 4
    if hero_r.right < 0: # 4
        hero_r.left = 800 # 4
    hero_r.y += player_gravity
    if hero_r.bottom >= 300:
        hero_r.bottom = 300
    screen.blit(hero_s, hero_r)
    screen.blit(snail_s, snail_r)
    snail_r.x -= 4
    if snail_r.right <= 0:
        snail_r.left = 800
    pygame.display.update()
    clock.tick(60)
