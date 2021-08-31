# Önceki videolarda sürekli statik resimler gördük bu sefer dinamik(hareketli) bir imaj yapacağız.
# Aslında biz hiç bir zaman statik bir görüntü yansıtmadık görüntüler loop da kalıp herhangi
# bir değişiklik olmadığı için statikmiş gibi gözüküyor yoksa resimler sürekli yenileniyor fakat
# bizim gözümüz bunu göremiyor.Burda bu özellikten yararlanacağız.
# while loop undaki objenin hareket etmesi için pozisyonunu sürekli değiştireceğiz.

import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
image_sky_surface = pygame.image.load("graphics/Sky.png")
image_ground_surface = pygame.image.load("graphics/ground.png")
text_surface_font = pygame.font.Font("font/Pixeltype.ttf",50)
text_surface = text_surface_font.render('My game',False,(0,0,0))
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    pygame.display.update()
    clock_object.tick(60)
