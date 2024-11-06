import pygame
import math
import colorsys

pygame.init()

black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 14
y_separator = 12

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 2, 2

theta_spacing = 3
phi_spacing = 9

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
animation_font = pygame.font.SysFont('Arial', 14, bold=True)
pause_font = pygame.font.SysFont('Arial', 24, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(letter, x_start, y_start):
    text = animation_font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    screen.blit(text, (x_start, y_start))

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
                    text_x = 1800
                    text_y = 1030
                    screen.blit(pause_text, (text_x, text_y))
                    print(pause_text)
                    pygame.display.update()

        

    if not animationpaused:

        screen.fill((black))
        z = [0] * screen_size
        b = [' '] * screen_size

        for j in range(0, 330, theta_spacing):
            for i in range(0, 450, phi_spacing):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                p = math.sin(i)
                h = d + 7
                D = 5 / (c * h * e * p + f * g  + 12)
                l = math.cos(i)
                q = math.sin(j)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(x_offset + 12 * D * (l * h * m - t * n + m * q))
                y = int(y_offset + 5 * D * (l * h * m - t * m / D * q))
                o = int(x + columns * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g + l * d * n))
                if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                    z[o] = D
                    b[o] = chars[N if N > 0 else 0]

        if y_start == rows * y_separator - y_separator:
            y_start = 0

        for i in range(len(b)):
            A += 0.000004
            B += 0.000001
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
Functions:
    hsv2rgb(h, s, v): Converts HSV color values to RGB.
    text_display(letter, x_start, y_start): Renders a letter on the screen at the specified coordinates.
Global Variables:
    black: RGB value for the color black.
    hue: Initial hue value for color transitions.
    WIDTH: Width of the Pygame window.
    HEIGHT: Height of the Pygame window.
    x_start, y_start: Starting coordinates for text rendering.
    x_separator: Horizontal spacing between characters.
    y_separator: Vertical spacing between characters.
    rows: Number of rows in the grid.
    columns: Number of columns in the grid.
    screen_size: Total number of cells in the grid.
    x_offset: Horizontal offset for the donut's center.
    y_offset: Vertical offset for the donut's center.
    A, B: Rotation angles for the donut.
    theta_spacing: Spacing for the theta angle in the donut's parametric equation.
    phi_spacing: Spacing for the phi angle in the donut's parametric equation.
    chars: Characters used to render the donut.
    screen: Pygame display surface.
    display_surface: Pygame display surface (duplicate).
    animation_font: Font used for rendering the animation.
    pause_font: Font used for rendering the pause text.
    run: Boolean to control the main loop.
    animationpaused: Boolean to control the animation state.
Main Loop:
    Handles Pygame events for quitting and pausing the animation.
    Updates the screen with the rotating donut animation when not paused.
    Renders the pause text when the animation is paused.
"""