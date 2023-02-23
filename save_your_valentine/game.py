#!/usr/bin/env python3

import sys
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Set window size and title
window_size = (1200, 800)
width = window_size[0]
height = window_size[1]
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Quiz des Super Héros")
song = pygame.mixer.Sound("correct.wav")
music_game = pygame.mixer.Sound("song_game.wav")
music_game.play()
# Load font
font = pygame.font.Font(None, 36)

# Function to draw text on the screen
def draw_text(text, x, y, font=font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Load background image
background = pygame.image.load("./background.jpg")
background = pygame.transform.scale(background, window_size)

# change opacity of background image
background.set_alpha(128)

# Display background
window.blit(background, (0, 0))
# Display Title
draw_text("Quiz des Super Héros", width // 2, 100)
draw_text("Êtes vous vraiment fan des super héros Marvel ?", width // 2, 300)
draw_text("Testez vos connaissances en répondant à ce quiz !", width // 2, 350)
draw_text("Cliquez sur Start pour commencer !", width // 2, 400)
rect = pygame.draw.rect(window, (255, 215, 0), (width // 2 - 100, 600, 200, 50), border_radius=10)
draw_text("Start", width // 2, 620, color=(0, 0, 0))
pygame.display.update()

# Check if user clicked on the start button
start = False
while not start:
    mouse = pygame.mouse.get_pos()
    if rect.collidepoint(mouse):
        rect = pygame.draw.rect(window, (255, 0, 0), (width // 2 - 100, 600, 200, 50), border_radius=10)
        draw_text("Start", width // 2, 620, color=(0, 0, 0))
    else:
        rect = pygame.draw.rect(window, (255, 215, 0), (width // 2 - 100, 600, 200, 50), border_radius=10)
        draw_text("Start", width // 2, 620, color=(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_x, mouse_y):
            # Change color of start button
            rect = pygame.draw.rect(window, (255, 255, 0), (width // 2 - 100, 600, 200, 50), border_radius=10)
            if event.type == pygame.MOUSEBUTTONUP:
                start = True
                break
    pygame.display.update()

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
    },
    {
        "question" : "Qui est le super-héros qui a des pouvoirs de télékinésie et de téléportation ?",
        "answers": ["Cyclope", "Magneto", "Cyclone", "Storm"],
        "correct": "Cyclope"
    },
    {
        "question": "Qui est l'ennemi juré de Spiderman ?",
        "answers": ["Green Goblin", "Venom", "Lizard", "Doctor Octopus"],
        "correct": "Green Goblin"
    },
    {
        "question": "Qui est le fondateur des Avengers ?",
        "answers": ["Captain America", "Iron Man", "Thor", "Hulk"],
        "correct": "Iron Man"
    },
    {
        "question": "Qui est le leader des X-Men ?",
        "answers": ["Professor X", "Wolverine", "Cyclops", "Jean Grey"],
        "correct": "Professor X"
    },
    {
        "question": "Quel est le vrai nom de Captain America ?",
        "answers": ["Tony Stark", "Steve Rogers", "Bruce Banner", " Peter Parker"],
        "correct": "Steve Rogers"
    },
    {
        "question": "Qui est le père de Thor ?",
        "answers": ["Odin", "Loki", "Heimdall", " Sif"],
        "correct": "Odin"
    },
    {
        "question": "Qui est le personnage joué par Robert Downey Jr. dans les films de l'univers cinématographique Marvel?",
        "answers": ["Thor", "Iron Man", "The Hulk"],
        "correct": "Iron Man"
    },
    {
        "question": "Qui est le membre fondateur des Avengers qui n'est pas un super-héros ?",
        "answers": ["Nick Fury", "Jarvis", "Happy Hogan"],
        "correct": "Nick Fury"
    },
    {
        "question": "Qui est considéré comme le leader original des Avengers ?",
        "answers": ["Nick Fury", "Iron Man", "Captain America", "Thor"],
        "correct": "Captain America"
    }
]

# Keep track of the number of correct answers
correct_answers = 0

# Loop through the quiz questions
for i, question_dict in enumerate(quiz):

    # Clear the screen
    window.fill((0, 0, 0))
    # Display background
    background.set_alpha(128)
    window.blit(background, (0, 0))

    # Display question number
    draw_text(f"Question {i + 1}/{len(quiz)}", width // 2, 100)

    # Display score
    draw_text(f"Score: {correct_answers}/{i}", width // 2, 150)

    # Wait for user to click on an answer
    correct_answer = question_dict["correct"]
    user_answer = None
    running = True
    while not user_answer:
        # Draw the question
        question = question_dict["question"]
        draw_text(question, width //2, height //2 - 100)
        
        # Draw the answers
        answers = question_dict["answers"]
        answer_rects = []
        x = 85
        mouse = pygame.mouse.get_pos()
        for i, answer in enumerate(answers):
            x += 250
            y = height // 2
            if x > width - 250:
                x = 600
                y = height // 2 + 150
            answer_rect = pygame.draw.rect(window, (0, 0, 0), (x-100, y-25, 200, 50), border_radius=10)
            if answer_rect.collidepoint(mouse):
                answer_rect = pygame.draw.rect(window, (255,0,0), answer_rect,border_radius=10)
                draw_text(answer, x, y) 
            else:
                answer_rect = pygame.draw.rect(window, (255,215,0), answer_rect,border_radius=10)
                draw_text(answer, x, y)
            answer_rects.append(answer_rect)
            pygame.display.update()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for k, answer_rect in enumerate(answer_rects):
                    if answer_rect.collidepoint(mouse_x, mouse_y):
                        user_answer = answers[k]
                        if user_answer == correct_answer:
                            song.play()
                            correct_answers += 1
                        break
                break
        pygame.display.flip()



# Clear the screen
window.fill((0, 0, 0))

# Display background
background.set_alpha(128)
window.blit(background, (0, 0))

# Display score
draw_text(f"Score: {correct_answers}/{len(quiz)}", width // 2, 150)

# Display final message
if correct_answers == len(quiz):
    draw_text("Bravo ! Vous êtes un vrai fan des super héros Marvel !", width // 2, 300)
elif correct_answers >= len(quiz) // 2:
    draw_text("Pas mal ! Vous connaissez bien les super héros Marvel !", width // 2, 300)
else:
    draw_text("Vous connaissez peut-être les super héros Marvel...", width // 2, 300)
    draw_text("Mais il vous faut plus d'entrainement !", width // 2, 350)

pygame.display.update()

# Wait for user to click on the screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()