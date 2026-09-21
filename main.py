import pygame
import sys
import os
import configparser
from periodic_table_data import *

# Initialize the parser
config = configparser.ConfigParser()
config.read('.config')
version = config.get('VERSION', 'version')

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 1300, 600  # Width to accommodate 18 columns
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Atomic Atlas")

# Colors
BACKGROUND_COLOR = (30, 30, 30)
DEFAULT_ELEMENT_COLOR = (160, 32, 240)  # Default button color
HIGHLIGHT_COLOR = (100, 100, 255)
TEXT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)
atomic_number_font = pygame.font.Font(None, 18)  # Smaller font for atomic numbers

# Button dimensions
button_width = 60
button_height = 60
padding = 10    

# Calculate total width of the buttons
total_width = 18 * (button_width + padding) - padding

# Track which element is selected
selected_element = None
show_details = False

# Function to draw element buttons
def draw_elements():
    for element in elements:
        x, y = element["pos"]
        rect = pygame.Rect(
            (WIDTH - total_width) // 2 + x * (button_width + padding),  # Center the buttons horizontally
            y * (button_height + padding) + padding,
            button_width,
            button_height
        )

        # Use the individual button colors
        if rect.collidepoint(pygame.mouse.get_pos()):
            color = HIGHLIGHT_COLOR
        else:
            color = element["button_color"]  # Use the element's button color

        # Draw the button rectangle
        pygame.draw.rect(screen, color, rect)

        # Draw the element symbol
        text = font.render(element["symbol"], True, element["text_color"])  # Use the element's text color
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

        # Draw the atomic number in the top left corner
        atomic_number_text = atomic_number_font.render(str(element["atomic_number"]), True, BLACK)
        atomic_number_rect = atomic_number_text.get_rect(topleft=(rect.left + 5, rect.top + 5))
        screen.blit(atomic_number_text, atomic_number_rect)

    # Detect clicks and check for element selection
    if pygame.mouse.get_pressed()[0]:  # Left mouse button click
        for element in elements:
            x, y = element["pos"]
            rect = pygame.Rect(
                (WIDTH - total_width) // 2 + x * (button_width + padding),
                y * (button_height + padding) + padding,
                button_width,
                button_height
            )
            if rect.collidepoint(pygame.mouse.get_pos()):
                return element
    return None

# Function to wrap text
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        # Check if adding the next word would exceed the max width
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)  # Add the last line
    return lines

def draw_element_details(element):
    screen.fill(BACKGROUND_COLOR)

    # Display element name, atomic number, atomic weight, category, state, isotopes, and description
    title = title_font.render(f"{element['name']} ({element['symbol']})", True, TEXT_COLOR)
    screen.blit(title, (50, 50))

    atomic_number_text = font.render(f"Atomic Number: {element['atomic_number']}", True, TEXT_COLOR)
    screen.blit(atomic_number_text, (50, 100))

    atomic_weight_text = font.render(f"Atomic Weight: {element['atomic_weight']}", True, TEXT_COLOR)
    screen.blit(atomic_weight_text, (50, 130))

    category_text = font.render(f"Category: {element['category']}", True, TEXT_COLOR)
    screen.blit(category_text, (50, 160))

    state_text = font.render(f"State at Room Temp: {element['state']}", True, TEXT_COLOR)
    screen.blit(state_text, (50, 190))

    isotopes_text = font.render("Isotopes: " + ", ".join(element["isotopes"]), True, TEXT_COLOR)
    screen.blit(isotopes_text, (50, 220))

    # Wrap and display description text
    description_lines = wrap_text(element['description'], font, 300)  # Wrap text within 600 pixels
    description_y = 250
    for line in description_lines:
        description_text = font.render(line, True, TEXT_COLOR)
        screen.blit(description_text, (50, description_y))
        description_y += 25  # Adjust line spacing as needed

    # Load and display atom image
    atom_image_path = element.get("image", "")
    if os.path.exists(atom_image_path):
        atom_image = pygame.image.load(atom_image_path)
        atom_image = pygame.transform.scale(atom_image, (150, 150))  # Resize to 150x150
        screen.blit(atom_image, (400, 100))  # Position the image on the screen
        
        # Display description for the normal atom image
        atom_desc_text = font.render(f"{element['name']} Atom", True, TEXT_COLOR)
        screen.blit(atom_desc_text, (400, 260))  # Position below the atom image
    else:
        print(f"Image not found: {atom_image_path}")  # Handle the missing image

    # Load and display isotope images
    for i, isotope in enumerate(element["isotopes"]):
        isotope_image_path = element["isotope_images"][i] if i < len(element["isotope_images"]) else ""
        if os.path.exists(isotope_image_path):
            isotope_image = pygame.image.load(isotope_image_path)  # Load isotope image
            isotope_image = pygame.transform.scale(isotope_image, (150, 150))  # Resize to 150x150
            screen.blit(isotope_image, (400 + i * 160, 300))  # Position images with some spacing

            # Get isotope name from isotope_names if it exists, else use the isotope symbol
            isotope_name = element["isotope_names"][i] if i < len(element["isotope_names"]) and element["isotope_names"][i] else isotope
            isotope_desc_text = font.render(f"Isotope: {isotope_name}", True, TEXT_COLOR)
            screen.blit(isotope_desc_text, (400 + i * 160, 460))  # Position below each isotope image
        else:
            print(f"Isotope image not found: {isotope_image_path}")  # Handle the missing isotope image

    # Add a back button in the top left corner
    back_button_rect = pygame.Rect(50, 500, 100, 40)
    pygame.draw.rect(screen, DEFAULT_ELEMENT_COLOR, back_button_rect)
    back_text = font.render("Back", True, TEXT_COLOR)
    screen.blit(back_text, back_button_rect.move(20, 10))

    return back_button_rect



version_text = font.render(f"Only natural isotopes. Early access v{version}", True, BLACK)
version_rect = version_text.get_rect()
version_rect.bottomright = (screen.get_width() - 10, screen.get_height() - 10)

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if in details view or main view
    if show_details and selected_element:
        # Draw the details of the selected element
        back_button_rect = draw_element_details(selected_element)

        # Check for back button click to go back to main screen
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                show_details = False
                selected_element = None
    else:
        # Draw the periodic table buttons and detect selection
        selected_element = draw_elements()
        if selected_element:  # If an element was clicked, switch to details view
            show_details = True

    screen.blit(version_text, version_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
