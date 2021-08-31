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
test_surface = pygame.Surface((100,200))# surface with plain color,Bu objenin tuple şeklinde bir parametreye ihtiyacı var.tuple ın içine width ve height gireceğiz.
test_surface.fill("Red") # yüzeyin rengini kırmızı yapıyor
test_surface.fill((0,100,100)) #bu şekilde de yazılabilir.
# not normalde fill in içine 3 elemanlı tuple girerek de rengi belirleyebiliriz onun listesi internette var.
clock_object = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(200,100)) #screen.blit in içine oynatmak istediğimiz surface ı ve poziyonunun tuple şeklinde giriyoruz.
    # bu yüzeyin ekranda gözükmesini sağlıyor.#fakat böyle bırakırsan birşey gözükmez çünkü rengi siyah olduğu için gözükmez
    # 0,0 ekranın sol en üst köşesi birinic değer widdth artırıldığında ekranın sol tarafından uzaklaşıp sağ tarafına yaklaşır.
    # ikinici değer height artırılısa ekranın alt tarafına yaklaşır.
    pygame.display.update()
    clock_object.tick(60)