# Ses ekleme
# pygamede ses eklemek basit
# pygame.mixer.Sound() kullanacağız.
# buna değişken atayacağız ardından değişkeni play edeceğiz
# x = pygame.mixer.Sound()
# x.play()#loops yazarak ne kadar süre oynatılacağına karar verebilirsin.
# eğer -1 yazarsan pygame bunu sürekli oynatır.
# ayrıca sesini de x.set_volume() ile ayaralayabilirsin.
# 1 maximum 0 minimum(sessiz) değerini gösterir aradaki kesirli değerler sesi verir.
# sakın while loop un içine yazma ses dosyaları çakışır oyüzden ya event loop a yaz yada
import pygame

from random import randint, choice

pygame.init()


class Player(pygame.sprite.Sprite):  # sprite.Sprite ı inherit ediyoruz.
    def __init__(self):
        super().__init__()  # super kullanarak inherit ediyoruz.
        # surfaceları buraya yazıyoruz.
        walk1 = pygame.image.load("graphics/Player/player_walk_1.png")
        walk2 = pygame.image.load("graphics/Player/player_walk_2.png")
        self.jump = pygame.image.load("graphics/Player/jump.png")
        self.walk = [walk1, walk2]
        self.index = 0
        self.gravity = 0
        self.image = self.walk[0]  # self.image ve self.rect özel instancelar onlar pygame tarafından otomatik
        # oynatılacak oyüzden bunları kullanma # fakat diğer instnclar özel değil benim atadığımı isimler.
        self.rect = self.image.get_rect(midbottom=(100, 300))
        self.emre_jump_m = pygame.mixer.Sound("audio/jump.mp3") # 1
        self.emre_jump_m.set_volume(0.15) # 1

    # Diğer özellikleri buraya dağıtıyoruz.
    def gravity_p(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom > 300:
            self.rect.bottom = 300

    def jump_f(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.emre_jump_m.play() # 1
            self.gravity = -20

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.index += 0.1
            if self.index >= len(self.walk): self.index = 0
            self.image = self.walk[int(self.index)]

    # ardından bu özellikleri update e yazıyoruz. ve while klasınını içinde groupe.update yapıyoruz.
    # update de özel bir method isminin update olamsı lazım

    def update(self):
        self.jump_f()
        self.gravity_p()
        self.animation()


class Obstacles(pygame.sprite.Sprite):
    # Aynı şeyler bu sınıf için de geçerli ayrıca göründüğü gibi
    # birden fazla farklı görüntüdeki şekli de aynı class ın içinde topluyabiliyoruz.
    # ve karakterlerin hızlı hareket etmesi için bug olmaması için 2 ye bölerek yazdık surfaceları
    def __init__(self, n_type):
        super().__init__()
        if n_type == "Fly":
            fly1 = pygame.image.load("graphics/Fly/Fly1.png")
            fly2 = pygame.image.load("graphics/Fly/Fly2.png")
            self.frames = [fly1, fly2]
        else:
            snail1 = pygame.image.load("graphics/snail/snail1.png")
            snail2 = pygame.image.load("graphics/snail/snail2.png")
            self.frames = [snail1, snail2]
        self.image = self.frames[0]
        if n_type == "Fly":
            self.rect = self.image.get_rect(bottomleft=(randint(900, 1100), randint(100, 200)))
        else:
            self.rect = self.image.get_rect(bottomleft=(randint(900, 1100), 300))
        self.index = 0

    def animation(self):
        self.index += 0.1
        if self.index >= 2:
            self.index = 0
        self.image = self.frames[int(self.index)]

    def move(self):
        if self.rect.right <= 0:
            self.kill()  # self.kill() özel bir fonksiyon sprite classının objesinin ölmesini sağlıyor.
        else:
            self.rect.x -= 5

    def update(self):
        self.animation()
        self.move()


# Sound
musiki = pygame.mixer.Sound("audio/music.wav") # 2
musiki.set_volume(0.4) # 2
musiki.play(-1) # 2
# Mains
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# Surfaces
ground_s = pygame.image.load("graphics/ground.png")
sky_s = pygame.image.load("graphics/Sky.png")

# Classes Groups
# Ardından bunlardan elde ettiğimiz objeleri grouplara aktarıyoruz.
# Eğerki sadece 1 tane obje yer alacaksa singlegroup birden fazla yer alacaksa groupe açılır.
pl = Player()
player_group = pygame.sprite.GroupSingle(pl)
obstacles = pygame.sprite.Group()
event1 = pygame.USEREVENT + 1
pygame.time.set_timer(event1, 1500)

# Score
score = 0
last_score = 0
font = pygame.font.Font("font/Pixeltype.ttf", 50)
score_s = font.render(f"Score:{score}", False, (64, 64, 64))
score_r = score_s.get_rect(bottomleft=(400, 400))

font1 = pygame.font.Font("font/Pixeltype.ttf", 35)
font2 = pygame.font.Font("font/Pixeltype.ttf", 60)
my_game_s = font.render("My Game", False, (64, 64, 64))
my_game_r = my_game_s.get_rect(midtop=(400, 0))

game_active = False


# Side Screen
def side_screen():
    a = pygame.image.load("graphics/Player/player_stand.png")
    a = pygame.transform.scale2x(a).convert_alpha()
    a_r = a.get_rect(center=(400, 200))
    b = font1.render("Press space to start the game", False, (111, 196, 169)).convert()
    c = font2.render("PixelRunner", False, (111, 196, 169)).convert()
    b.get_rect()
    c.get_rect()
    screen.fill((94, 129, 162, 0))
    screen.blit(a, a_r)
    screen.blit(c, c.get_rect(midbottom=(a_r.centerx + 5, a_r.top - 20)))
    screen.blit(b, b.get_rect(center=(a_r.centerx, a_r.bottom + 35)))
    score_s = font.render(f"Score:{score // 1000}", False, (64, 64, 64))
    screen.blit(score_s, score_s.get_rect(center=(a_r.centerx, a_r.bottom + 70)))


def play_check():
    if pygame.sprite.spritecollide(player_group.sprite, obstacles, False):  # aynı zamanda pygame.sprite.spritecollide
        # ile collisionları kontrol edebiliriz.eğer collision varsa 2 groupe arasında evet dönderir.
        return False
    return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == event1:
                obstacles.add(Obstacles(choice(["Fly", "Snail", "Snail"])))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    last_score = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                last_score = pygame.time.get_ticks()

    if game_active:
        # Score
        score = pygame.time.get_ticks() - last_score
        score_s = font.render(f"{score // 1000}", False, (64, 64, 64))

        # Blit operations
        screen.blit(sky_s, (0, 0))
        screen.blit(ground_s, (0, 300))
        screen.blit(score_s, score_r)
        pygame.draw.rect(screen, "#c0e8ec", my_game_r, 0, 6)
        screen.blit(my_game_s, my_game_r)
        player_group.draw(screen)  # grouplardaki objeleri çizmek için draw kullanıyoruz.
        obstacles.draw(screen)
        # Update
        player_group.update()  # ardından grouplardakileri hareket ettirmek ve güncellemek için groupename.update i
        # kullanıyoruz.
        obstacles.update()
        game_active = play_check()
    else:
        pl.rect.bottom = 300
        obstacles.empty()  # groupname.empty() de özel bir methoddur.grubun içini boşaltmayı sağlar.
        side_screen()
    clock.tick(60)
    pygame.display.update()
