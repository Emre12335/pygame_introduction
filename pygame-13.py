import pygame

pygame.init()
# İşlem 1
# timer tanımlıyoruz.
ot = pygame.USEREVENT + 1  # event çeşidi
pygame.time.set_timer(ot, 900)

# New obstacle logic düşmanların rastgele olarak çıkmasını sağlamak için 1/ İçinde rectanglelar içerecek bir liste
# oluşturacağız. 2/ her defasında yeni rectanglelar ekleyeceğiz. 3/ o listedeki her elemanı ekrana yansıtıp bütün
# rectangle ları sola kaydıracağız.eğer listedeki herhangi bir rectangle ekrandan çıkarsa listeden çıkarcağız.
# anlatıcı 3. aşamayı gerçekleştirirken fonksiyon tanımlamayı tercih ediyor.
# Eski işlemler temeli
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400))
snail_s = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
fly_s = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
ground_s = pygame.image.load("graphics/ground.png").convert()
sky_s = pygame.image.load("graphics/Sky.png").convert()
# 1/obstacle list'i oluşturduk
ol = []

# 3 enemyleri spawn ediyoruz ve eğer 0 dan küçük olursa
def spawn_enemies(liste):
    if len(liste) != 0:
        for member in liste:
            if member.bottom == 300:
                screen.blit(snail_s, member)
            else:
                screen.blit(fly_s, member)
            member.x -= 5
        liste = [m for m in liste if m.right > 0]
        return liste
    return []


from random import randint

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == ot:  # 2 event.type her ot olduğunda o listeye eleman ekleyeceğiz.
            if randint(0, 2):
                ol.append(snail_s.get_rect(bottomleft=(randint(900, 1100), 300)))  # bunu yapmamızın sebebi
            else:
                ol.append(fly_s.get_rect(midbottom=(randint(900, 1100), randint(100, 299))))
    screen.blit(sky_s, (0, 0))
    screen.blit(ground_s, (0, 300))
    ol = spawn_enemies(ol)  # 3 enemyleri spawn ediyoruz ve yeni listeyi eski listeye atıyoruz.
    pygame.display.update()
    clock.tick(60)
