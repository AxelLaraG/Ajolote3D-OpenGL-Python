import sys
import pygame
from pygame_menu import MenuBar

# Crea una ventana
window = pygame.display.set_mode((640, 480))

# Crea una barra de menú
menubar = MenuBar()

# Agrega un elemento de menú a la barra de menú
file_menu = menubar.add_item("Archivo")

# Añade la barra de menú a la ventana
window.set_menubar(menubar)

# Bucle principal del juego
while True:

    # Maneja eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualiza la pantalla
    pygame.display.flip()

