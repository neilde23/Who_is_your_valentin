# app/interface.py

__version__ = 'V.0.0.1'
__name__ = 'Comet Game'
__author__ = 'Flavien HUGS'


import math, sys, pygame

from app.game import Game


def main():
    FPSCLOCK = 60
    pygame.init()
    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1080, 700))
    pygame.display.set_caption("BAT FALL GAME".upper())

    background = pygame.image.load("src/bg.jpg").convert()
    background = pygame.transform.scale(background, (1080, 700))
    background_position = background.get_rect()
    background_position.x = 0
    background_position.y = 0

    bg = pygame.image.load("background.png").convert()
    bg = pygame.transform.scale(bg, (1080, 700))
    bg_position = bg.get_rect()
    bg_position.x = 0
    bg_position.y = 0

    #diminiution de l'opacity de l'image
    background.set_alpha(128)

    banner = pygame.image.load("src/banner.png")
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    play_button = pygame.image.load("src/button.png")
    play_button = pygame.transform.scale(play_button, (400, 400))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2) - 50

    game = Game()

    while True:
        screen.fill((0, 0, 0))

        if game.is_playing:
            screen.blit(bg, bg_position)
            game.start_game(screen)
        else:
            screen.blit(background, background_position)
            screen.blit(play_button, play_button_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    if game.is_playing:
                        game.player.launch_weapon()
                    else:
                        game.start()
                        game.sound_manager.play('click')
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.start()
                    game.sound_manager.play('click')

        fps_clock.tick(FPSCLOCK)
        pygame.display.update()
