import pygame
pygame.init()
# Artık ekran fazla kalabalık olmaya başladığı için bu ekranı kullanacağız.
# demo olması için.

# pygame de yeni bir konsept öğreneceğiz ismi timer
# işlevi ise bazı kodları belirli bir zaman dilimlerinde oynatmayı sağlamak.
# bunu sağlamak için ise
# 1/ Yeni bir event çeşidi oluşturacağız.
# 2/ Bu event çeşidini for loop un içine yazacağız.
# 3/ Gerçekleştirmek istediğmiz işlemleri oraya yazacağız.


# İşlem 1
# timer tanımlıyoruz.
ot = pygame.USEREVENT + 1 # event çeşidi
pygame.time.set_timer(ot,900) # bu event çeşidinin her 900 saniyede bir gerçekleşeceğini söyledik.
# bunu herhangi bir variable atamadan yapmış olduk.
# +1 deme sebebimiz USEREVENT e ayrılan bazı işlmeler zaten var oyüzden  her yeni timer yazarken +1 ekleyeceğiz
# örneğin 2.bir timer yazacaksak pygame.USEREVENT + 2 dememiz gerekiyor.


# Eski işlemler temeli
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # İşlem 2 for loop un içinde ona özel bir event.type yazıyoruz.
        if event.type == ot:
            # İşlem 3 yapmak istediğimiz kodu içine giriyoruz.
            print("Sistem 1")
    pygame.display.update()
    clock.tick(60)

# Bu bilgiyi spawn oluşturmak için nasıl kullanacağız pygame-13 de.
