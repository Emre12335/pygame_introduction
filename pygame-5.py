# Collision

# rectangleları kullanabildiğimiz bir diğer nokta collision adını verdiğmiz 2 farklı surface ın kesişme noktaları .
# sadece 2 rectangle ın değil rectangle'ın mouse ile kesişimi ve mouse ın sol tıkı ile kesişimi de tespit edilebilir.
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
rectange_main_hero_surface = main_hero_surface.get_rect(midbottom=(80,300))
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():#collision ı mouse ile yapmanın bir diğer yöntemi ise  event iledir.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION: #mouse hareket halinde ise pozisyonun gösterir
            print(event.pos)
            if rectange_main_hero_surface.collidepoint(event.pos):
                print("Kesisişim")
        if event.type == pygame.MOUSEBUTTONDOWN:#tıkladığımızda down yazıyor
            print("down")
        if event.type == pygame.MOUSEBUTTONUP:#tıkdan çektiğinde up
            print("up")

    screen.blit(image_sky_surface,(0,0))
    screen.blit(image_ground_surface,(0,300))
    screen.blit(text_surface,(350,20))
    screen.blit(snail_surface,rectangle_snail)
    rectangle_snail.x -= 4
    if rectangle_snail.right <= 0:
        rectangle_snail.left = 800
    screen.blit(main_hero_surface,rectange_main_hero_surface)
    if rectange_main_hero_surface.colliderect(rectangle_snail): # bu doğru yanlış gönderir oyüzden bunu if ile yazabiliriz.
        print("collision") # bu şekilde istediğimzi işlemi gerçekleştirebiliriz.
    # collidepoint belirli bir x ve y pozisyonuna geldiğinde rectangle da true verir yani collision gösterir.Belirli
    # bir posizyona gelip gelmediğine bakmak için bunu kullanırız.
    if rectange_main_hero_surface.collidepoint(pygame.mouse.get_pos()):# içine x ve y girilir normalde fakat bunun yerine mouse un pozisyonunu alacağız.
        print(pygame.mouse.get_pressed(3))#bu özellik hangi tuşa bastığını gösteriyor.mouseda

    pygame.display.update()
    clock_object.tick(60)

