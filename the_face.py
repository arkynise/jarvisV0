import pygame
import sys
import subprocess
import os
import win32gui, win32api

# Initialize Pygame
pygame.init()

# Set up display
width, height = 150, 150
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

# Set up colors
BLACK = (0, 0, 0)

# Ball properties
max_radius = 70
min_radius = 60
ball_radius = min_radius

# Ball position
ball_x = width // 2
ball_y = height // 2
font = pygame.font.Font(None, 100)  # Choose font and size
character_text = "J"

# Function to read color data from a file
def read_color():
    try:
        with open("color.txt", "r") as file:
            color_data = file.read().strip()
            return tuple(map(int, color_data.split(",")))
    except FileNotFoundError:
        # Create the file with default color if it doesn't exist
        default_color = (255, 0, 0)  # Default color: red
        write_color(default_color)
        return default_color

# Function to write color data to a file
def write_color(color_data):
    with open("color.txt", "w") as file:
        file.write(",".join(map(str, color_data)))

# Zooming direction

def render_alphabet_centered(surface, font, text, color, center):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    surface.blit(text_surface, text_rect)
zoom_in = True

# Main loop
dragging=False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass


        if pygame.mouse.get_pressed()[0]: 
            x, y = win32api.GetCursorPos()
            hwnd = pygame.display.get_wm_info()["window"]
            win32gui.MoveWindow(hwnd, x-100, y-100, width, height, True)
 

              


    # Read color data from file
    ball_color = read_color()

    # Zoom in and out
    if zoom_in:
        ball_radius += 0.5  # Adjust zooming rate
        if ball_radius >= max_radius:
            zoom_in = False
    else:
        ball_radius -= 0.5  # Adjust zooming rate
        if ball_radius <= min_radius:
            zoom_in = True

    # Clear the screen
    screen.fill((0, 0, 0, 100))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), int(ball_radius))
    render_alphabet_centered(screen, font, character_text, BLACK, (ball_x, ball_y))

    # Update the display
    pygame.display.flip()

    # Control the speed of updates
    pygame.time.delay(40)  # Adjust this value as needed

# Quit Pygame
pygame.quit()
sys.exit()
process = subprocess.Popen(['python', 'main.py'])
print(process.pid)

os.kill(process.pid, signal.SIGINT)