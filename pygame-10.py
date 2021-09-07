# Oyunu durdurma ve ara geçiş ekranı tasarlama
# oyunu durdurmak için variable kullanacağız.
# bu variable True iken oyun dönecek False iken ise
# menü ekranını split edecek.
# space tuşuna basıldığında yada mouse ile ekranın orta bölgesine basıldığında ise
# oyun yeniden başlayacak.
# menü ekranını düzenlerken
# ortada büyük bir logo olmasını istiyoruz etrafında ise mavi bir ekran bunu ayarlamak için ise
# screen.fill ve scratch gibi ögeler kullanmamız gerekecek.
# ekran tasarımını statik olacak şekilde oyundan bağlantısız olarak burda yapacağız.


import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Menu")
# Surface
main = pygame.image.load("graphics/Player/player_stand.png")
# transfrom(büyüklüğünü) ayarlamak için temel yollar rotatezoom ve scale
# scale tuple girildiği zaman en ve boy büyütor bu sayede ekran büyüyor.
# rotatezoom da aynı mantıkta tek farkı angle yani şeklin kaç derece açıyla yerleştiriliceğine de karar verebiliyorsun.
# bu sayede şekli istersen tam ters istersen 30 derece kayık vaziyette de koyabilirsin.
# scale in büyüklük ayarı tuple iken rotozoom un float/int dir.
# rotate ise sadece açıyı değiştirmek için var
# rotozoom görüntünün kalitesini scale e göre 1 tık daha iyi korur.
main1 = pygame.transform.scale2x(main)
main2 = pygame.transform.scale(main,(150,150))
main4 = pygame.transform.rotate(main,180)
main3 = pygame.transform.rotozoom(main,0,2)
main_rect = main3.get_rect(center = (400,200))

font = pygame.font.Font("font/Pixeltype.ttf",35)
font2 = pygame.font.Font("font/Pixeltype.ttf",60)
font_s = font.render("Press space to start the game",False,(111,196,169)).convert_alpha()
font_s_2 = font2.render("PixelRunner",False,(111,196,169)).convert_alpha()

font_s_r = font_s.get_rect(center = (main_rect.centerx,main_rect.bottom+35))
font_s_r_2 = font_s_2.get_rect(midbottom = (main_rect.centerx + 5,main_rect.top-20))

while True:
    screen.fill((94,129,162))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(main3,main_rect)
    screen.blit(font_s,font_s_r)
    screen.blit(font_s_2,font_s_r_2)
    pygame.display.update()
