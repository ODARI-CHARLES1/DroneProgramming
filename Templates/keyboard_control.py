import pygame

pygame.init()

win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Keyboard Controller")

SPEED = 50

def get_keyboard_input():

    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    pygame.event.pump()
    keys = pygame.key.get_pressed()

    # A/D -> Left Right
    if keys[pygame.K_a]:
        left_right = -SPEED
    elif keys[pygame.K_d]:
        left_right = SPEED

    # W/S -> Forward Backward
    if keys[pygame.K_w]:
        forward_backward = SPEED
    elif keys[pygame.K_s]:
        forward_backward = -SPEED

    # Arrow Up/Down -> Altitude
    if keys[pygame.K_UP]:
        up_down = SPEED
    elif keys[pygame.K_DOWN]:
        up_down = -SPEED

    # Arrow Left/Right -> Yaw
    if keys[pygame.K_LEFT]:
        yaw = -SPEED
    elif keys[pygame.K_RIGHT]:
        yaw = SPEED

    return [left_right, forward_backward, up_down, yaw]