# Creating window in pygame,

import pygame
pygame.init() # Bu pygame in kurulmasını sağlıyor.Pygame ile çalışmaya başlamadan önce mutlaka kurmak gerek.
# pygame deki özelliklerin çoğu module tabanlı oyüzden 2-3 noktalı çok ifade var.

screen = pygame.display.set_mode((800,400))#pygame.display module ü ekranla igili işlemlerde kullanıyoruz.set_mode en az 1 parametre almak
# zorunda ve bu parametre tuple halinde olmak zorunda height ve width olmak üzere 2 tane değer giriyoruz.

# tkinter daki gibi pygame de mainloop yok çünkü tkinter dakinden farklı olarak resimler arası geçişler olacak oyüzden.
# oynattığımız pencerenin açık kalması için while loop açıyoruz.

while True:
    pass