# Önceki videolarda sürekli statik resimler gördük bu sefer dinamik(hareketli) bir imaj yapacağız.
# Aslında biz hiç bir zaman statik bir görüntü yansıtmadık görüntüler loop da kalıp herhangi
# bir değişiklik olmadığı için statikmiş gibi gözüküyor yoksa resimler sürekli yenileniyor fakat
# bizim gözümüz bunu göremiyor.Burda bu özellikten yararlanacağız.
# while loop undaki objenin hareket etmesi için pozisyonunu sürekli değiştireceğiz.

import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
image_sky_surface = pygame.image.load("graphics/Sky.png").convert() # convert_uygulandı/5
image_ground_surface = pygame.image.load("graphics/ground.png").convert() # convert_uygulandı/5
text_surface_font = pygame.font.Font("font/Pixeltype.ttf",50)
text_surface = text_surface_font.render('My game',False,(0,0,0)).convert() # convert_uygulandı/5
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha() # snail surface eklendi/1
# alpha_convert_uygulandı/5
x_position = 780 # snail in ana pozisyonu.
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    screen.blit(snail_surface,(x_position,260)) # snail ekrana yansıtıldı/2
    x_position -= 4 # bu piksel hızı tick ile birlikte hızı belirliyorlar frame başı 4 birim gidecek/3
    # bu şekilde bırakırsak snail negatif yönünde gider ve bir daha gözükmez bunu engellemek için if koşulu ekleyeceğiz.
    if x_position == -100: # /4
        x_position = 780
    pygame.display.update()
    clock_object.tick(60)

# Son olarak bütün surfacelara convert işlemi yapacağız bunun sebebi surfacelardaki imagelar imageları surface'a
# çevirsek bile ekranda kullanılabilir hale gelmesi için ara işlemden geçiyor.Bu oyunda bug oluşmasına sebebiyet
# verebiliyor.Hedef bunun önüne geçmek.hepsine convert işlemi yapacağız.Eğer image alpha value dediğmiz özel bir
# value içeriyorsa dönüşürken sıkıntı yaşanabiliyor bunun için convert_alpha kullanacağız snail surface'ında./5
