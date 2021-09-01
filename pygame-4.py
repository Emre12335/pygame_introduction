# rectangles
# rectangles ın 2 tane görevi var pygame de surfaceları ekrana yerleştirmek ve collisionları önlemek(
# sonraki dersin konusu) surfaceları ekrana yerleştirirken zorlanabiliriz.çünkü image yada surfacelarda yerleştirilen
# nokta en tepe sol noktası. bu da spesifik olarak salyangozu yere yerleştirmeyi zorlaştırıyor.Bunu engellemek için
# rectangle kullanacağız.Bu sayede resmin istersek taban noktasının istersek tepe noktasını seçip rahatça
# yerleştirebileceğiz.
import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
image_sky_surface = pygame.image.load("graphics/Sky.png").convert()
image_ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface_font = pygame.font.Font("font/Pixeltype.ttf",50)
text_surface = text_surface_font.render('My game',False,(0,0,0)).convert()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
x_position = 780
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    screen.blit(snail_surface,(x_position,260))
    x_position -= 4
    if x_position == -100:
        x_position = 780
    pygame.display.update()
    clock_object.tick(60)
