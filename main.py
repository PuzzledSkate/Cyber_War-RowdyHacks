import pygame
from locations import *

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber War - RowdyHacks")
FPS = 60
clock = pygame.time.Clock()

# Static Variables
WIDTH = 900
HEIGHT = 500
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_BIG = pygame.font.Font('freesansbold.ttf', 32)
FONT_SMALL = pygame.font.Font('freesansbold.ttf', 20)

# Player 1 text
player1Text = FONT_BIG.render('Player 1', True, WHITE, BLACK)
player1TextRect = player1Text.get_rect()
player1TextRect.center = (800, int(HEIGHT/2) + 50)
Opt1 = FONT_BIG.render('1. Attack', True, WHITE, BLACK)
player1Opt1Rect = Opt1.get_rect()
player1Opt1Rect.center = (800, int(HEIGHT/2) + 100)
Opt2 = FONT_BIG.render('2. Skip   ', True, WHITE, BLACK)
player1Opt2Rect = Opt2.get_rect()
player1Opt2Rect.center = (800, int(HEIGHT/2) + 150)
# Player 2 text
player2Text = FONT_BIG.render('Player 2', True, WHITE, BLACK)
player2TextRect = player2Text.get_rect()
player2TextRect.center = (800, 50)
player2Opt1Rect = Opt1.get_rect()
player2Opt1Rect.center = (800, 100)
player2Opt2Rect = Opt2.get_rect()
player2Opt2Rect.center = (800, 150)


# Draws all pygame images to screen
def redraw_window():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, int((HEIGHT-10)/2), 900, 10))
    draw_servers()
    draw_firewalls()
    draw_2fa()
    draw_attacks()
    draw_text()
    pygame.display.update()


# Defines where servers are drawn
def draw_servers():
    pygame.draw.rect(screen, GREEN, BOTTOM_SERVER_ONE)
    pygame.draw.rect(screen, GREEN, BOTTOM_SERVER_TWO)
    pygame.draw.rect(screen, GREEN, BOTTOM_SERVER_THREE)
    pygame.draw.rect(screen, GREEN, BOTTOM_SERVER_FOUR)
    pygame.draw.rect(screen, GREEN, BOTTOM_SERVER_FIVE)
    pygame.draw.rect(screen, GREEN, TOP_SERVER_ONE)
    pygame.draw.rect(screen, GREEN, TOP_SERVER_TWO)
    pygame.draw.rect(screen, GREEN, TOP_SERVER_THREE)
    pygame.draw.rect(screen, GREEN, TOP_SERVER_FOUR)
    pygame.draw.rect(screen, GREEN, TOP_SERVER_FIVE)


# Defines where firewalls are drawn
def draw_firewalls():
    pygame.draw.rect(screen, YELLOW, BOTTOM_FIREWALL_ONE, 5)
    pygame.draw.rect(screen, YELLOW, BOTTOM_FIREWALL_TWO, 5)
    pygame.draw.rect(screen, YELLOW, BOTTOM_FIREWALL_THREE, 5)
    pygame.draw.rect(screen, YELLOW, BOTTOM_FIREWALL_FOUR, 5)
    pygame.draw.rect(screen, YELLOW, BOTTOM_FIREWALL_FIVE, 5)
    pygame.draw.rect(screen, YELLOW, TOP_FIREWALL_ONE, 5)
    pygame.draw.rect(screen, YELLOW, TOP_FIREWALL_TWO, 5)
    pygame.draw.rect(screen, YELLOW, TOP_FIREWALL_THREE, 5)
    pygame.draw.rect(screen, YELLOW, TOP_FIREWALL_FOUR, 5)
    pygame.draw.rect(screen, YELLOW, TOP_FIREWALL_FIVE, 5)


# Defines where 2FA Shields are drawn
def draw_2fa():
    pygame.draw.rect(screen, BLUE, BOTTOM_2FA_ONE, 5)
    pygame.draw.rect(screen, BLUE, BOTTOM_2FA_TWO, 5)
    pygame.draw.rect(screen, BLUE, TOP_2FA_ONE, 5)
    pygame.draw.rect(screen, BLUE, TOP_2FA_TWO, 5)


# Defines where attack bubbles are drawn
def draw_attacks():
    pygame.draw.circle(screen, RED, BOTTOM_ATTACK_ONE, 20, 5)
    pygame.draw.circle(screen, RED, BOTTOM_ATTACK_TWO, 20, 5)
    pygame.draw.circle(screen, RED, BOTTOM_ATTACK_THREE, 20, 5)
    pygame.draw.circle(screen, RED, BOTTOM_ATTACK_FOUR, 20, 5)
    pygame.draw.circle(screen, RED, TOP_ATTACK_ONE, 20, 5)
    pygame.draw.circle(screen, RED, TOP_ATTACK_TWO, 20, 5)
    pygame.draw.circle(screen, RED, TOP_ATTACK_THREE, 20, 5)
    pygame.draw.circle(screen, RED, TOP_ATTACK_FOUR, 20, 5)


# Defines where text is drawn
def draw_text():
    if turn == 1:
        screen.blit(player1Text, player1TextRect)
        screen.blit(Opt1, player1Opt1Rect)
        screen.blit(Opt2, player1Opt2Rect)
    else:
        screen.blit(player2Text, player2TextRect)
        screen.blit(Opt1, player2Opt1Rect)
        screen.blit(Opt2, player2Opt2Rect)


# Main function and main game loop
def main():
    run = True
    keys = pygame.key.get_pressed()
    global turn
    turn = 1

    while run :
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        if turn == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        turn = 2
                        print("Hit")
                    elif event.key == pygame.K_2:
                        turn = 2
                        print("Skip")
                if event.type == pygame.QUIT:
                    run = False

        elif turn == 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        turn = 1
                        print("Hit")
                    elif event.key == pygame.K_2:
                        turn = 1
                        print("Skip")
                if event.type == pygame.QUIT:
                    run = False

        redraw_window()


if __name__ == "__main__":
    main()
