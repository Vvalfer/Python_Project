import pygame
import math
import colorsys

pygame.init()

"""background"""

black = (0, 0, 0)

"""couleur animation"""
hue = 0 


"""taille de l'écran"""
WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

"""espacement entre les lettres"""
x_separator = 12
y_separator = 22

"""nombre de lignes et de colonnes de la grille"""
rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

"""offset pour le centre du donut"""
x_offset = columns / 2
y_offset = rows / 2

"""angles de rotation"""
A, B = 1, 2


theta_spacing = 7
phi_spacing = 3

"""caractères utilisés pour le rendu"""
chars = "Ryan;Louis,!"


screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
animation_font = pygame.font.SysFont('Arial', 14, bold=True)
pause_font = pygame.font.SysFont('Arial', 24, bold=True)

"""Main Loop"""
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

"""text display"""
def text_display (letter, x_start, y_start):
    text = animation_font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

run = True
animationpaused = False


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animationpaused = not animationpaused
                if animationpaused:
                    pause_text = pause_font.render("Pause", True, (255, 0, 0))
                    text_x = 2
                    text_y = 2
                    screen.blit(pause_text, (text_x, text_y))
                    print(pause_text)
                    pygame.display.update()
    """animation"""
    if not animationpaused:

        screen.fill((black))

        z = [0] * screen_size
        b = [' '] * screen_size

        for j in range(0, 628, theta_spacing):
            for i in range(0, 628, phi_spacing):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int (x_offset + 40 * D * (l *h * m - t * n))
                y = int (y_offset + 20 * D * (l *h * m - t * m))
                o = int(x + columns * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                    z[o] = D
                    b[o] = chars[N if N > 0 else 0]

        if y_start == rows * y_separator - y_separator:
            y_start = 0

        """affichage des lettres"""
        for i in range (len(b)):
            A += 0.000003
            B += 0.000002
            if i == 0 or i % columns:
                text_display(b[i], x_start, y_start)
                x_start += x_separator
            else:
                y_start += y_separator
                x_start = 0
                text_display(b[i], x_start, y_start)
                x_start += x_separator


        pygame.display.update()

        hue += 0.009

"""
This script creates an animated donut using Pygame. The animation can be paused and resumed using the spacebar.
Modules:
pygame: Used for creating the graphical display and handling events.
math: Provides mathematical functions.
colorsys: Used for converting HSV color values to RGB.
Functions:
hsv2rgb(h, s, v):
    Converts HSV color values to RGB.
    Parameters:
        h (float): Hue value.
        s (float): Saturation value.
        v (float): Value (brightness).
    Returns:
        tuple: Corresponding RGB values.
text_display(letter, x_start, y_start):
    Renders and displays a letter on the screen at the specified coordinates.
    Parameters:
        letter (str): The character to display.
        x_start (int): The x-coordinate for the text position.
        y_start (int): The y-coordinate for the text position.
Variables:
black (tuple): RGB values for the color black.
hue (float): Initial hue value for color animation.
WIDTH (int): Width of the display window.
HEIGHT (int): Height of the display window.
x_start (int): Initial x-coordinate for text display.
y_start (int): Initial y-coordinate for text display.
x_separator (int): Horizontal spacing between characters.
y_separator (int): Vertical spacing between characters.
rows (int): Number of rows in the display grid.
columns (int): Number of columns in the display grid.
screen_size (int): Total number of grid cells.
x_offset (float): Horizontal offset for the donut's center.
y_offset (float): Vertical offset for the donut's center.
A (float): Angle A for the donut's rotation.
B (float): Angle B for the donut's rotation.
theta_spacing (int): Spacing for theta angle increments.
phi_spacing (int): Spacing for phi angle increments.
chars (str): Characters used for rendering the donut.
Pygame Initialization:
Initializes Pygame, sets up the display window, and defines fonts for text rendering.
Main Loop:
Handles events such as quitting the application and pausing the animation.
Updates the display with the animated donut when not paused.
"""