#!/usr/bin/env python3

import sys
import pygame

# Initialize Pygame
pygame.init()

# Set window size and title
window_size = (1200, 800)
width = window_size[0]
height = window_size[1]
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Quiz des Super Héros")

# Load font
font = pygame.font.Font(None, 36)

# Dictionary of questions and answers
quiz = {
    "Nom du premier super héros créé par DC Comics": "Superman",
    "Quel est le vrai nom de Batman": "Bruce Wayne",
    "Quel est le pouvoir de Wonder Woman": "Force et agilité surhumaines, expert en combat à mains nues et avec des armes",
    "Quel est le super vilain ennemi de Spider-Man": "Green Goblin",
    "Quel est le vrai nom de Captain America": "Steve Rogers"
}

# Function to draw text on the screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, window_size)

# Display background
window.blit(background, (0, 0))

# Display question and answers
question = "Quel est le nom du super-héros qui a les ailes d'un cygne et la force d'un lion ?"
draw_text(question, width //2, height //2 - 100)

answers = ["Wonder Woman", "Superman", "Cyclone", "Hawkwoman"]
answer_rects = []
x = 85
for i, answer in enumerate(answers):
    x += 250
    if x > width - 250:
        x = 335
        y = height // 2 + 50
    y = height // 2
    answer_rect = pygame.draw.rect(window, (), (x-100, y-25, 200, 50), 2, border_radius=10)
    draw_text(answer, x, y)
    answer_rects.append(answer_rect)

pygame.display.update()

# Wait for user to click on an answer
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, answer_rect in enumerate(answer_rects):
                if answer_rect.collidepoint(mouse_x, mouse_y):
                    print("Vous avez sélectionné la réponse", answers[i])


# Start the quiz
start_quiz()
