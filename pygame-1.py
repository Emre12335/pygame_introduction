# Creating window in pygame,

import pygame

pygame.init()  # Bu pygame in kurulmasını sağlıyor.Pygame ile çalışmaya başlamadan önce mutlaka kurmak gerek.
# pygame deki özelliklerin çoğu module tabanlı oyüzden 2-3 noktalı çok ifade var.

screen = pygame.display.set_mode(
    (800, 400))  # pygame.display module ü ekranla igili işlemlerde kullanıyoruz.set_mode en az 1 parametre almak
# zorunda ve bu parametre tuple halinde olmak zorunda height ve width olmak üzere 2 tane değer giriyoruz.

pygame.display.set_caption("OYUN1")#oyunun ismi bu şekilde değiştirilebilir.

# tkinter daki gibi pygame de mainloop yok çünkü tkinter dakinden farklı olarak resimler arası geçişler olacak oyüzden.
# oynattığımız pencerenin açık kalması için while loop açıyoruz.

import sys

while True:
    # Tkinterdakinden farklı olarak açılan pencerede kapatma tuşu çalışmıyor.Bu yüzden kendi kapatma tuşumumz for loop ile ekliyoruz.
    for event in pygame.event.get():  # pygame.event.get() kullanıcının girdilerini kontrol ediyor.
        if event.type == pygame.QUIT:  # eğer event çık komutu ise pygame i kapat diyoruz.
            pygame.quit()  # pygame.quit() pygame.init() in tam tersi
            sys.exit()  # ardından loopdan çıkması için break yerine exit() kullanıyoruz

    # Resimlerde yaptığımz değişikliklerin kaydedilmesi için while loop u sürekli yeniliyoruz. Yoksa sabit kalır.
    pygame.display.update()
