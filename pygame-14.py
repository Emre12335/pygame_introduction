# Bu ders 12 ve 13 de öğrendiğimiz şeyleri kobinleyeceğiz.
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
# 1 userevent oluşturacapız
obs_t = pygame.USEREVENT + 1
# 2 userevent i 1500 milisaniyeye ayarlayacağız.
pygame.time.set_timer(obs_t, 1500)
# 4 enemyleri spawn etmek için liste oluşturacağız.
obs_l = []


# 6 spawn ettiğimiz rectleri surface ile birlikte ekrana yansıtacağız.
# 7 fly da spawn edebilmek için ot ye rastgele olarak 100,300 yüksekliği arası flylar ekleyeceğiz.
def spawn_enemies(new_list: list) -> list:
    if len(new_list) != 0:
        for member in new_list:
            if member.bottom == 300:
                screen.blit(snail_s, member)
            else:
                screen.blit(fly_s, member)  # fly ı y eksenine göre ayırdım
            member.x -= 5
        new_list = [m for m in new_list if m.right > 0]
        return new_list
    else:
        return []


# 8 rectangleların temasını kontrol etmek için
def game_stop(new_list):
    global player_r
    if not new_list:
        return True
    for member in new_list:
        if player_r.colliderect(member):
            return False
    return True


# Fonts for text surfaces
my_game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
# Surfaces/PlayScreen
sky_s = pygame.image.load("graphics/Sky.png").convert()
ground_s = pygame.image.load("graphics/ground.png").convert()
snail_s = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
fly_s = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
player_s = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
my_game_s = my_game_font.render("My Game", False, (64, 64, 64)).convert()

# Rectangles/PlayScreen
snail_r = snail_s.get_rect(bottomleft=(800, 300))
player_r = player_s.get_rect(midbottom=(100, 300))
my_game_r = my_game_s.get_rect(midtop=(400, 10))

# Variables
gravity = 0
game_play = False
# score variables
score = 0
old_score = 0
# score surface-rectangles
score_s = my_game_font.render(f"{score}", False, (64, 64, 64))
score_r = score_s.get_rect(midbottom=(400, 400))

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
            if event.type == obs_t:  # 3 event.type yazıldı
                # 7 fly ekliyoruz
                if randint(0, 2):  # integer 0 olursaa false 1 yada 2 olursa True olucak
                    obs_l.append(snail_s.get_rect(bottomleft=(randint(900, 1100), 300)))  # 5 timer her tetiklendğinde
                    # yeni bir rect.angle ekliyoruz.
                else:
                    obs_l.append(fly_s.get_rect(bottomleft=(randint(900, 1100), randint(100, 250))))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_play = True
                    old_score = pygame.time.get_ticks()
                    # altta yazan sebebin aynısı bura için de geçerli.
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_play = True
                old_score = pygame.time.get_ticks()  # old score u buraya bu şekilde yazmamızın sebebi
                # bu buraya kaydedildikten sonra yenilenmeyecek olması yani score hep sabit kalacak
                # sadece oyun durup yeniden başladığında güncellenecek.
    # Game on
    if game_play:
        # Blit area
        screen.blit(sky_s, (0, 0))
        screen.blit(ground_s, (0, 300))
        screen.blit(my_game_s, my_game_r)
        screen.blit(player_s, player_r)
        obs_l = spawn_enemies(obs_l)
        screen.blit(score_s, score_r)

        # Draw
        pygame.draw.rect(screen, "#c0e8ec", my_game_r, 16, 6)
        screen.blit(my_game_s, my_game_r)
        # Gravity
        gravity += 1
        player_r.y += gravity
        if player_r.bottom > 300:
            player_r.bottom = 300
        # Score board update
        score = pygame.time.get_ticks() - old_score
        score_s = my_game_font.render(f"{score // 1000}", False, (64, 64, 64)).convert()
        # Game active check
        game_play = game_stop(obs_l)
    # Game off
    else:
        # Oyun yeniden başladığında list i boşaltıyoruz.
        obs_l = []
        player_r.bottom = 300
        gravity = 0
        score_s2 = my_game_font.render(f"score:{score // 1000}", False, (64, 64, 64)).convert()
        score_s2_r = score_s2.get_rect(center=(pixelspace_r.centerx, pixelspace_r.bottom + 25))
        # Blit
        screen.fill((94, 129, 162))
        screen.blit(player_s_menu, player_s_menu_r)
        screen.blit(pixel, pixel_r)
        screen.blit(pixelspace, pixelspace_r)
        screen.blit(score_s2, score_s2_r)

    # Display and Clock
    clock.tick(60)
    pygame.display.update()
