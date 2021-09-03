# boyama yapma işlemi sanılanın aksine rectanglelar ile gerçekleştirilmez.
# pygame.draw.rect(),pygame.draw.ellipse,.. gibi  fonksiyonlar kullanılarak ve seçlilen yüzeyin üstüne konum girilerek
# belirlenir.rectangle dikdörtgen demek olduğu için belirtilen konuma dikdörtgen
# hazır kodda font u rectangle ile yerleştirdik ve pygame-5 deki collisionları attık.
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
ground_surface = pygame.image.load("graphics/ground.png").convert()
sky_surface = pygame.image.load("graphics/Sky.png").convert()
font_type = pygame.font.Font("font/Pixeltype.ttf", 50)
text_surface = font_type.render("My Game", False, (0, 0, 0)).convert()
text_rect  = text_surface.get_rect(midtop = (400,0))
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
hero_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomleft=(800, 300))
hero_rectangle = hero_surface.get_rect(midbottom=(100, 300))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen,"#c0e8ec",text_rect)#rectangleları bu şekilde renklendirebilirsin.
    pygame.draw.rect(screen,"#c0e8ec",text_rect,6)#rectangle dikdörtgen demek oyüzden dikdörtgen
    pygame.draw.line(screen,(0,0,0),(0,0),(800,400),5)#line ile lines aynı işlemi yapar tek farkı biri düz ve bozukluklrı azaltılmış diğeri daha bozuk
    pygame.draw.aaline(screen , (0,0,0),(0,400),(800,0),5)
    pygame.draw.lines(screen,(0,0,0),False,[(50,0),(50,400),(100,200),(100,150)],10)#lines ise birden fazla çizgi çekmeyi sağlıyor.
    pygame.draw.aalines(screen,(0,0,0),True,[(750,0),(750,400),(700,200),(700,150)],10)#True ise sonuncuyu birleşitirip kapalı şekil yapıyor.
    #yoksa açık bırakıyor.
    pygame.draw.circle(screen,"Red",(400,200),radius=100,width=2)
    pygame.draw.circle(screen,"Blue",(400,200),radius=50)#width içinin dolu olup olmamasını,radius ise büyüklüğünü gösteriyor.
    pygame.draw.arc(screen,"Yellow",hero_rectangle,30,40,100)
    pygame.draw.polygon(screen,"Pink",[(0,0),(100,0),(100,100),(100,200),(200,100)])
    pygame.draw.ellipse(screen,"Green",hero_rectangle,0)
    screen.blit(text_surface,text_rect)
    screen.blit(snail_surface, snail_rectangle)
    screen.blit(hero_surface, hero_rectangle)
    snail_rectangle.x -= 4
    if snail_rectangle.right == 0:
        snail_rectangle.left = 800
    clock.tick(60)
    pygame.display.update()

# Bu şekilde istediğin şekli çizebilirsin.
# pygamede 2 farklı renk seçme yöntemi var rgb ve code.
# red green blue  ve code yöntemi
# red green blue tuple şeklinde girdiğimiz  renk kodu
# code ise direk renk kodunu "#c34bfet" gibi girdiğimiz ifadeler.
# rgb pygame e özel bir renk kodlama biçimi tupledaki rakamların büyüklüğü arttıkça giren renk miktarı artıyor.
# örneğin (0,0,0) red = 0, green = 0, blue = 0 iken
# (10,10,10) red = 10, green = 10,blue = 10 gibi düşünülebilir.
# codeise direk internetten bul yapıştır.

