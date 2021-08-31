# Surfaces in pygame

# pygame de herhangi birşey nasıl çizilip ekrana yansıtılır?
# bunun için yüzey(surface kullanılır.)
# temel anlamda 2 tane yüzey vardır pygamede.1)Display surface/2)regular surface
# display surface oyunun oynandığı ve kullanıcıya sunulan ekrandır.
# fakat pygame de herhangi bir text i direk ekrana bastıramayız öncesinde bunun içinbir yüzeye ihtiyacımız var.
# bunlara regular surface denir.bir resmi ekranda göstermek istiyorsam öncesinde mutlaka resmi bir yüzeye koymalıyım ardından yüzeyi
# display ekranında göstermeliyim.Bu yüzeyin üzerine koyacağımız şey herhangi bir şey olabilir. text color görüntü.Ve genelde 1 den fazla
# görüntü için birden fazla surface kullanılır.Bu yüzeylerde yaptığımız işlemler ekrana yansıtmadığımız sürece gözükmez.
# display surface 1 tanedir sürekli gözükür.regular surface ise birden fazladır. ve özükmeyebilir.

import pygame
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
image_sky_surface = pygame.image.load("graphics/Sky.png")
image_ground_surface = pygame.image.load("graphics/ground.png")
text_surface_font = pygame.font.Font("font/Pixeltype.ttf",50) # font un içine yazılan şeyler 1.si font type 2.si font size
# None yazarsak default olan tipi kullanırız. # Fakat biz
text_surface = text_surface_font.render('My game',False,(0,0,0)) # font yazıldıktan sonra render ile bunu ana surface a yazıyoruz.
# bunun parametreleri 1.text 2.Yumuşatma fontu(piksel tipi olduğu için false dedik) 3.Renk siyah istediğimiz için 0,0,0 dedik

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