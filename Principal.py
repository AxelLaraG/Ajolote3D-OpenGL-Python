import pygame
import Ajolote as aj
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os

# Variables para el control del mouse
rotating = False
prev_mouse_x = 0
prev_mouse_y = 0
rotation_speed = 0.5

#Identifica si el sonido de fondo se está reproduciendo
fondo=False

# Bandera para fondos
cont = 0

# Bandera para sonidos
band = 10

# Inicializa Pygame
pygame.init()

# Arreglo de Sonidos
sound = []
for i in os.listdir("Sounds"):
    if i.endswith(".wav"):
        sonido = pygame.mixer.Sound(os.path.join("Sounds", i))
        sound.append(sonido)

# Configura la ventana Pygame
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Ajolote:Lara Madero Axel 19280766   Gestos:H,E,T,M,I,L,K   Movimientos:C,A,D,P,O,V,K,S   Otros:+,-,flecha Izq y Der")

# Configura la perspectiva OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Inicializar diccionario de eventos
keys = {
    "C": False, #Mov 1
    "H": False, #Gesto 1
    "A": False, #Mov 2
    "D": False, #Mov 3
    "E": False, #Gesto 2
    "T": False, #Gesto 3
    "M": False, #Gesto 4
    "I": False, #Gesto 5
    "L": False, #Gesto 6
    "P": False, #Mov 4
    "O": False, #Mov 5
    "V": False, #Mov 6
    "K": False, #Gesto 7
}

# Matriz de raices
fondos = [
    "fondos/0.jpg",  # 0
    "fondos/1.jpg",  # 1
    "fondos/2.jpg",  # 2
    "fondos/3.jpg",  # 3
    "fondos/4.jpg",  # 4
    "fondos/5.jpg",  # 5
    "fondos/6.jpg",  # 6
    "fondos/7.jpg",  # 7
    "fondos/8.jpg",  # 8
    "fondos/9.jpg",  # 9
    "fondos/10.jpg",  # 10
    "fondos/11.jpg",  # 11
    "fondos/12.jpg",  # 12
    "fondos/13.jpg",  # 13
    "fondos/14.jpg",  # 14
]

texture_background = pygame.image.load(fondos[2])
texture_left_right = pygame.image.load(fondos[0])
texture_top_bottom = pygame.image.load(fondos[1])


# Cargando las texturas
def inicializarTexturas(fondo_NB, fondo_NLR, fondo_NTB):
    global texture_left_right, texture_background, texture_top_bottom
    texture_background = pygame.image.load(fondos[fondo_NB])
    texture_left_right = pygame.image.load(fondos[fondo_NLR])
    texture_top_bottom = pygame.image.load(fondos[fondo_NTB])


# Función para manejar los eventos del mouse
def handle_mouse_events(event):
    global rotating, prev_mouse_x, prev_mouse_y

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Botón izquierdo del mouse
            rotating = True
            prev_mouse_x, prev_mouse_y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            rotating = False
    elif event.type == pygame.MOUSEMOTION and rotating:
        delta_x = event.pos[0] - prev_mouse_x
        delta_y = event.pos[1] - prev_mouse_y
        prev_mouse_x, prev_mouse_y = event.pos
        glRotatef(delta_x * rotation_speed, 0, 1, 0)
        glRotatef(delta_y * rotation_speed, 1, 0, 0)


# Reestablecer eventos de Mouse
def reloadKeys():
    global keys
    for key in keys:
        keys[key] = False


# Función para cargar una textura OpenGL
def load_texture(texture_surface):
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGB,
        width,
        height,
        0,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        texture_data,
    )
    return texture_id


# Dibujar cubo de texturas
def texturas():
    # Establecimiento de texturas en formato OpenGL
    texture_background_id = load_texture(texture_background)
    texture_left_right_id = load_texture(texture_left_right)
    texture_top_bottom_id = load_texture(texture_top_bottom)
    # Dibuja un cubo con texturas
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_background_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-10, -10, -10)
    glTexCoord2f(1, 0)
    glVertex3f(10, -10, -10)
    glTexCoord2f(1, 1)
    glVertex3f(10, 10, -10)
    glTexCoord2f(0, 1)
    glVertex3f(-10, 10, -10)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_left_right_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-10, -10, -10)
    glTexCoord2f(1, 0)
    glVertex3f(-10, -10, 10)
    glTexCoord2f(1, 1)
    glVertex3f(-10, 10, 10)
    glTexCoord2f(0, 1)
    glVertex3f(-10, 10, -10)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_left_right_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(10, -10, -10)
    glTexCoord2f(1, 0)
    glVertex3f(10, -10, 10)
    glTexCoord2f(1, 1)
    glVertex3f(10, 10, 10)
    glTexCoord2f(0, 1)
    glVertex3f(10, 10, -10)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_top_bottom_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-10, 10, -10)
    glTexCoord2f(1, 0)
    glVertex3f(10, 10, -10)
    glTexCoord2f(1, 1)
    glVertex3f(10, 10, 10)
    glTexCoord2f(0, 1)
    glVertex3f(-10, 10, 10)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_top_bottom_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-10, -10, -10)
    glTexCoord2f(1, 0)
    glVertex3f(10, -10, -10)
    glTexCoord2f(1, 1)
    glVertex3f(10, -10, 10)
    glTexCoord2f(0, 1)
    glVertex3f(-10, -10, 10)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def inicializarBrillo():
    light_ambient = [0.9, 0.9, 0.9, 1.0]
    light_diffuse = [0.3, 0.3, 0.3, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    light_position = [1.0, 1.5, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

def stopSound():
    global fondo
    for i in range(0,13):
        if not(i == 9 and fondo):
            sound[i].stop()

def repSonido(bandera):
    stopSound()
    if bandera == 10:
        sound[0].play()
    if bandera == 11:
        sound[1].play()
    if bandera == 12:
        sound[2].play()
    if bandera == 13:
        sound[3].play()
    if bandera == 14:
        sound[4].play()
    if bandera == 15:
        sound[5].play()
    if bandera == 16:
        sound[6].play()
    if bandera == 17:
        sound[7].play()
    if bandera == 18:
        sound[8].play()
    if bandera == 19:
        sound[10].play()
    if bandera == 20:
        sound[11].play()
    if bandera == 21:
        sound[12].play()
    if bandera == 22:
        sound[13].play()
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            print()
            if event.key == pygame.K_MINUS:  # Zoom out
                glTranslatef(0, 0, -0.1)
            elif event.key == pygame.K_PLUS:  # Zoom in
                glTranslatef(0, 0, 0.1)
            elif event.key == pygame.K_s:
                if fondo:
                    sound[9].stop()
                    fondo=False
                else:
                    sound[9].play()
                    fondo=True
            elif event.key == pygame.K_RIGHT:  # Cambios de fondo hacia adelante
                if cont < 4:
                    cont += 1
                else:
                    cont = 0
            elif event.key == pygame.K_LEFT:  # Cambio de fondo hacia atrás
                if cont > 0:
                    cont -= 1
                else:
                    cont = 4
            else:
                val1=chr(event.key).upper() in keys
                val2=keys[chr(event.key).upper()] == False
                if val1 and val2:
                    reloadKeys()
                    keys[chr(event.key).upper()] = True
                    if band < 22:
                        repSonido(band)
                        band += 1
                    else:
                        repSonido(22)
                        band=10
                else:
                    keys[chr(event.key).upper()] = False
        
            if cont == 0:
                inicializarTexturas(2, 0, 1)
            elif cont == 1:
                inicializarTexturas(8, 5, 4)
            elif cont == 2:
                inicializarTexturas(3, 7, 9)
            elif cont == 3:
                inicializarTexturas(11, 10, 9)
            elif cont == 4:
                inicializarTexturas(12, 14, 8)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        texturas()
        inicializarBrillo()
        aj.dibujaAjolote(
            keys["C"],
            keys["H"],
            keys["A"],
            keys["D"],
            keys["E"],
            keys["T"],
            keys["M"],
            keys["I"],
            keys["L"],
            keys["P"],
            keys["O"],
            keys["V"],
            keys["K"],
        )
        handle_mouse_events(event)
        pygame.display.flip()
        pygame.time.wait(10)
