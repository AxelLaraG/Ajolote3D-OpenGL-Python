import pygame
import Ajolote as aj 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inicializa Pygame
pygame.init()

# Configura la ventana Pygame
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Ajolote")

# Fuente para el texto del menú
font = pygame.font.Font(None, 24)

#Inicializar arreglos de eventos
keys = [False] * 7

# Cargando las texturas
texture_background = pygame.image.load("fondos/1.jpg")
texture_left = pygame.image.load("fondos/2.jpg")
texture_right = pygame.image.load("fondos/2.jpg")
texture_top = pygame.image.load("fondos/3.jpg")
texture_bottom = pygame.image.load("fondos/3.jpg")

# Configura la perspectiva OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Variables para el control del mouse
rotating = False
prev_mouse_x = 0
prev_mouse_y = 0
rotation_speed = 0.5

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

#Reestablecer eventos de Mouse
def reloadKeys():
    for i in range(len(keys)):
        keys[i]=False

# Función para cargar una textura OpenGL
def load_texture(texture_surface):
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

#Dibujar cubo de texturas
def texturas():
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

    glBindTexture(GL_TEXTURE_2D, texture_left_id)
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

    glBindTexture(GL_TEXTURE_2D, texture_right_id)
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

    glBindTexture(GL_TEXTURE_2D, texture_top_id)
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

    glBindTexture(GL_TEXTURE_2D, texture_bottom_id)
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

#Establecimiento de texturas en formato OpenGL
texture_background_id = load_texture(texture_background)
texture_left_id = load_texture(texture_left)
texture_right_id = load_texture(texture_right)
texture_top_id = load_texture(texture_top)
texture_bottom_id = load_texture(texture_bottom)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            reloadKeys()
            if event.key == pygame.K_c:
                keys[0]=True
            elif event.key == pygame.K_h:
                keys[1]=True
            elif event.key == pygame.K_a:
                keys[2]=True
            elif event.key == pygame.K_d:
                keys[3]=True
            elif event.key == pygame.K_e:
                keys[4]=True
            elif event.key == pygame.K_t:
                keys[5]=True
            elif event.key == pygame.K_m:
                keys[6]=True
            elif event.key == pygame.K_MINUS:
                glTranslatef(0,0,-0.1)
            elif event.key == pygame.K_PLUS:
                glTranslatef(0,0,0.1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        texturas()   
        inicializarBrillo()     

        aj.dibujaAjolote(keys[0],keys[1],keys[2],keys[3],keys[4],keys[5],keys[6])
        
        handle_mouse_events(event)
        pygame.display.flip()
        pygame.time.wait(10)