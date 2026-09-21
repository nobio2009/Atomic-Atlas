import pygame
import sys
import os
import configparser
import json
from periodic_table_data import *  # your elements data

# --- Setup config ---
config = configparser.ConfigParser()
config.read('.config')
version = config.get('VERSION', 'version')

# --- Pygame init ---
pygame.init()
WIDTH, HEIGHT = 1300, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Atomic Atlas")

# Colors
BACKGROUND_COLOR = (30, 30, 30)
DEFAULT_ELEMENT_COLOR = (160, 32, 240)
HIGHLIGHT_COLOR = (100, 100, 255)
TEXT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)
atomic_number_font = pygame.font.Font(None, 18)

# Button sizes
button_width = 60
button_height = 60
padding = 10
total_width = 18 * (button_width + padding) - padding

# --- Notes directories ---
NOTES_DIR = "notes"
GENERAL_NOTES_FILE = os.path.join(NOTES_DIR, "general.md")
os.makedirs(NOTES_DIR, exist_ok=True)
if not os.path.exists(GENERAL_NOTES_FILE):
    with open(GENERAL_NOTES_FILE, "w", encoding="utf-8") as f:
        f.write("")

def get_element_notes_path(symbol):
    folder = os.path.join(NOTES_DIR, symbol)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "notes.md")  # default file

def get_notes_files(element=None):
    if element:
        folder = os.path.dirname(get_element_notes_path(element["symbol"]))
    else:
        folder = NOTES_DIR
    os.makedirs(folder, exist_ok=True)
    return [f for f in os.listdir(folder) if f.endswith(".md")]

def load_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def save_file(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# --- Wrapping helper ---
def wrap_text(text, font, max_width):
    """
    Wrap text to fit within max_width.
    - Preserves line breaks from the file.
    - Breaks long words properly.
    """
    lines = []
    # Split on actual newlines first
    for paragraph in text.splitlines():
        words = paragraph.split(' ')
        current_line = ''
        for word in words:
            # Include space between words
            test_line = current_line + (word + ' ')
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:  # Save finished line
                    lines.append(current_line.strip())
                # Start a new line with the long word
                current_line = word + ' '
        # Add the last line in the paragraph
        if current_line:
            lines.append(current_line.strip())
        # Blank line to match Markdown spacing
        if paragraph.strip() == '':
            lines.append('')

    return lines


# --- Draw periodic table ---
def draw_elements():
    for element in elements:
        x, y = element["pos"]
        rect = pygame.Rect(
            (WIDTH - total_width)//2 + x*(button_width+padding),
            y*(button_height+padding)+padding,
            button_width,
            button_height
        )
        color = HIGHLIGHT_COLOR if rect.collidepoint(pygame.mouse.get_pos()) else element["button_color"]
        pygame.draw.rect(screen, color, rect)
        text = font.render(element["symbol"], True, element["text_color"])
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
        atomic_number_text = atomic_number_font.render(str(element["atomic_number"]), True, BLACK)
        screen.blit(atomic_number_text, (rect.left+5, rect.top+5))

    if pygame.mouse.get_pressed()[0]:
        for element in elements:
            x, y = element["pos"]
            rect = pygame.Rect(
                (WIDTH - total_width)//2 + x*(button_width+padding),
                y*(button_height+padding)+padding,
                button_width,
                button_height
            )
            if rect.collidepoint(pygame.mouse.get_pos()):
                return element
    return None

# --- Draw element details ---
def draw_element_details(element):
    screen.fill(BACKGROUND_COLOR)
    title = title_font.render(f"{element['name']} ({element['symbol']})", True, TEXT_COLOR)
    screen.blit(title, (50, 50))

    screen.blit(font.render(f"Atomic Number: {element['atomic_number']}", True, TEXT_COLOR),(50,100))
    screen.blit(font.render(f"Atomic Weight: {element['atomic_weight']}", True, TEXT_COLOR),(50,130))
    screen.blit(font.render(f"Category: {element['category']}", True, TEXT_COLOR),(50,160))
    screen.blit(font.render(f"State at Room Temp: {element['state']}", True, TEXT_COLOR),(50,190))
    screen.blit(font.render("Isotopes: "+", ".join(element["isotopes"]), True, TEXT_COLOR),(50,220))

    # Wrap and display description text
    description_lines = wrap_text(element['description'], font, 600)  # or 1100
    y = 250
    for line in description_lines:
        rendered = font.render(line, True, TEXT_COLOR)
        screen.blit(rendered, (50, y))
        y += rendered.get_height() + 5
        

    atom_image_path = element.get("image","")
    if os.path.exists(atom_image_path):
        atom_image = pygame.image.load(atom_image_path)
        atom_image = pygame.transform.scale(atom_image, (150,150))
        screen.blit(atom_image,(400,100))
        screen.blit(font.render(f"{element['name']} Atom", True, TEXT_COLOR),(400,260))

    for i,isotope in enumerate(element["isotopes"]):
        if i < len(element["isotope_images"]):
            isotope_image_path = element["isotope_images"][i]
            if os.path.exists(isotope_image_path):
                isotope_image = pygame.image.load(isotope_image_path)
                isotope_image = pygame.transform.scale(isotope_image,(150,150))
                screen.blit(isotope_image,(400+i*160,300))
                isotope_name = element["isotope_names"][i] if i < len(element["isotope_names"]) and element["isotope_names"][i] else isotope
                screen.blit(font.render(f"Isotope: {isotope_name}", True, TEXT_COLOR),(400+i*160,460))

    back_button_rect = pygame.Rect(50,500,100,40)
    pygame.draw.rect(screen, DEFAULT_ELEMENT_COLOR, back_button_rect)
    screen.blit(font.render("Back", True, TEXT_COLOR), back_button_rect.move(20,10))

    notes_button_rect = pygame.Rect(170,500,100,40)
    pygame.draw.rect(screen, DEFAULT_ELEMENT_COLOR, notes_button_rect)
    screen.blit(font.render("Notes", True, TEXT_COLOR), notes_button_rect.move(20,10))

    return back_button_rect, notes_button_rect

# --- Draw notes list ---
def draw_notes_list(element=None):
    screen.fill(BACKGROUND_COLOR)
    folder = NOTES_DIR if not element else os.path.dirname(get_element_notes_path(element["symbol"]))
    title = "General Notes" if not element else f"Notes for {element['name']} ({element['symbol']})"
    screen.blit(title_font.render(title, True, TEXT_COLOR),(50,50))

    md_files = get_notes_files(element)
    file_rects=[]
    y=120
    for f in md_files:
        rect = pygame.Rect(50,y,400,30)
        pygame.draw.rect(screen,DEFAULT_ELEMENT_COLOR,rect)
        screen.blit(font.render(f,True,TEXT_COLOR),rect.move(10,5))
        file_rects.append((rect,os.path.join(folder,f)))
        y+=40

    new_button_rect = pygame.Rect(50,y+20,150,30)
    pygame.draw.rect(screen,DEFAULT_ELEMENT_COLOR,new_button_rect)
    screen.blit(font.render("+ New Note",True,TEXT_COLOR),new_button_rect.move(10,5))

    return file_rects,new_button_rect

# --- Draw note editor ---
def draw_note_editor(note_text,note_name):
    screen.fill(BACKGROUND_COLOR)
    screen.blit(title_font.render(f"Editing: {note_name}",True,TEXT_COLOR),(50,50))
    y=100
    for line in wrap_text(note_text,font,1000):
        screen.blit(font.render(line,True,TEXT_COLOR),(50,y))
        y+=25
    screen.blit(font.render("Type to edit. ESC to save and go back.",True,TEXT_COLOR),(50,y+40))

# --- State ---
selected_element=None
show_details=False
show_notes_list=False
editing_notes=False
current_note_path=""
note_text=""

version_text=font.render(f"Only natural isotopes. Early access v{version}",True,BLACK)
version_rect=version_text.get_rect()
version_rect.bottomright=(screen.get_width()-10,screen.get_height()-10)

# --- Main loop ---
running=True
while running:
    if editing_notes:
        draw_note_editor(note_text, os.path.basename(current_note_path))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    save_file(current_note_path,note_text)
                    editing_notes=False
                elif event.key==pygame.K_BACKSPACE:
                    note_text=note_text[:-1]
                elif event.key==pygame.K_RETURN:
                    note_text+="\n"
                else:
                    note_text+=event.unicode
        continue

    if show_notes_list:
        file_rects,new_button_rect=draw_notes_list(selected_element if show_details else None)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                for rect,path in file_rects:
                    if rect.collidepoint(pos):
                        note_text=load_file(path)
                        current_note_path=path
                        editing_notes=True
                        show_notes_list=False
                if new_button_rect.collidepoint(pos):
                    folder=NOTES_DIR if not selected_element else os.path.dirname(get_element_notes_path(selected_element["symbol"]))
                    new_name=f"note_{len(file_rects)+1}.md"
                    new_path=os.path.join(folder,new_name)
                    save_file(new_path,"")
                    note_text=""
                    current_note_path=new_path
                    editing_notes=True
                    show_notes_list=False
            elif event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                show_notes_list=False
        continue

    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    if show_details and selected_element:
        back_button_rect,notes_button_rect=draw_element_details(selected_element)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                show_details=False
                selected_element=None
            elif notes_button_rect.collidepoint(pygame.mouse.get_pos()):
                show_notes_list=True
    else:
        selected_element=draw_elements()
        if selected_element:
            show_details=True
        # Draw general notes button
        general_notes_button_rect=pygame.Rect(50,HEIGHT-60,100,40)
        pygame.draw.rect(screen,DEFAULT_ELEMENT_COLOR,general_notes_button_rect)
        screen.blit(font.render("Notes",True,TEXT_COLOR),general_notes_button_rect.move(20,10))
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if general_notes_button_rect.collidepoint(pygame.mouse.get_pos()):
                show_notes_list=True

    screen.blit(version_text,version_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
