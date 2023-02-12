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

# Function to draw text on the screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Load background image
background = pygame.image.load("./background.jpg")
background = pygame.transform.scale(background, window_size)
# Quiz questions and answers
quiz = [
    {
        "question": "Quel est le nom du super-héros qui a les ailes d'un cygne et la force d'un lion ?",
        "answers": ["Wonder Woman", "Superman", "Cyclone", "Hawkwoman"],
        "correct": "Hawkwoman"
    },
    {
        "question": "Quel est le nom du super-héros qui peut voler, a une vitesse surhumaine et une force surhumaine ?",
        "answers": ["Batman", "Superman", "Wonder Woman", "Cyclone"],
        "correct": "Superman"
    }
]

# Keep track of the number of correct answers
correct_answers = 0

# Loop through the quiz questions
for i, question_dict in enumerate(quiz):

    # Display background
    window.blit(background, (0, 0))

    # Draw the question
    question = question_dict["question"]
    draw_text(question, width //2, height //2 - 100)
    
    # Draw the answers
    answers = question_dict["answers"]
    answer_rects = []
    x = 85
    for i, answer in enumerate(answers):
        x += 250
        y = height // 2
        if x > width - 250:
            x = 600
            y = height // 2 + 150
        answer_rect = pygame.draw.rect(window, (255, 215, 0), (x-100, y-25, 200, 50), 2, border_radius=10)
        draw_text(answer, x, y)
        answer_rects.append(answer_rect)

    pygame.display.update()
    
    # Wait for user to click on an answer
    correct_answer = question_dict["correct"]
    user_answer = None
    while not user_answer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for k, answer_rect in enumerate(answer_rects):
                    if answer_rect.collidepoint(mouse_x, mouse_y):
                        user_answer = answers[k]
                        if user_answer == correct_answer:
                            correct_answers += 1
                        break
                break
