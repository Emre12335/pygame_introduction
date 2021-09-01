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
rectangle_snail = snail_surface.get_rect(bottomright = (600,300))
main_hero_surface =  pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
rectange_main_hero_surface = main_hero_surface.get_rect(midbottom=(80,300)) # get_rect haır keyword argument alır.
# topleft,midtop,topright/midleft,center,midright/bottomleft,midbottom,bottomright
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    screen.blit(snail_surface,rectangle_snail)
    rectangle_snail.x -= 4 # left ve right x ekseni olan uzunluğu print ediyor.(left,right,top,bottom ile karakterin konumu değiştirilebilir.)
    # top bottom center ise y ekseni olan uzunluğu print ediyor.(x ve y ile de değiştirilebilir.)
    # aşağı yukarı hareket ettirmek için top bottom center kullanacağız
    # sağa sola için ise left right ı kullanacağız.
    if rectangle_snail.right <= 0:
        rectangle_snail.left = 800
    screen.blit(main_hero_surface,rectange_main_hero_surface) # direk bu şekilde yerleştirebiliriz.

    pygame.display.update()
    clock_object.tick(60)
