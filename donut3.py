import pygame 
import math
import colorsys

pygame.init()

black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 12
y_separator = 23

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 4

chars = ".,-~:;=!*#$@"


screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
animation_font = pygame.font.SysFont('Arial', 14, bold=True)
pause_font = pygame.font.SysFont('Arial', 24, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


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


        for i in range (len(b)):
            A += 0.000005
            B += 0.000004
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
This script creates a rotating 3D donut animation using Pygame.
Modules:
    - pygame: Used for creating the graphical display and handling events.
    - math: Provides mathematical functions.
    - colorsys: Used for converting HSV color values to RGB.
Constants:
    - black: RGB value for the color black.
    - hue: Initial hue value for HSV color conversion.
    - WIDTH: Width of the display window.
    - HEIGHT: Height of the display window.
    - x_start, y_start: Starting coordinates for text display.
    - x_separator, y_separator: Separators for the grid layout.
    - rows, columns: Number of rows and columns in the grid.
    - screen_size: Total number of grid cells.
    - x_offset, y_offset: Offsets for centering the donut.
    - A, B: Rotation angles.
    - theta_spacing, phi_spacing: Spacing for theta and phi angles.
    - chars: Characters used for rendering the donut.
Functions:
    - hsv2rgb(h, s, v): Converts HSV color values to RGB.
    - text_display(letter, x_start, y_start): Renders a letter at the specified coordinates.
Main Loop:
    - Handles events such as quitting the application and pausing the animation.
    - Updates the display with the rotating donut animation.
    - Adjusts the hue for color cycling.
"""