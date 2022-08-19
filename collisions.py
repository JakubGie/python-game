def wall(player_position, player_position_before):
    wall = [
        [0, 0, 0, 800], #left side
        [735, 0, 735, 600], #right side
        [0, 0, 740, 0], #top
        [0, 535, 740, 535], #bottom
    ]

    for coordinates in wall:
        if player_position[0] >= coordinates[0] and player_position[1] >= coordinates[1] and player_position[0] <= coordinates[2] and player_position[1] <= coordinates[3]:
            for cords in range(0, 16):
                player_position[cords] = player_position_before[cords]

def monitoring(player_position, game_screen, screen, point):
    import pygame
    if game_screen == 1:
        for coordinates in objects:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (255, 0, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 2:
        for coordinates in objects2:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (255, 0, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 3:
        for coordinates in objects3:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (255, 0, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 4:
        for coordinates in objects4:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (255, 0, 0), (coordinates[0], coordinates[1], width, height))
    screen.blit(point, (player_position[0], player_position[1]))
    screen.blit(point, (player_position[2], player_position[3]))
    screen.blit(point, (player_position[4], player_position[5]))
    screen.blit(point, (player_position[6], player_position[7]))
    screen.blit(point, (player_position[8], player_position[9]))
    screen.blit(point, (player_position[10], player_position[11]))
    screen.blit(point, (player_position[12], player_position[13]))
    screen.blit(point, (player_position[14], player_position[15]))
    print(f"{player_position[0]} - {player_position[1]}")

def collision(player_position, player_position_before, game_screen):
    global objects, objects2, objects3, objects4
    objects = [
        [656, 0, 700, 190],
        [664, 420, 700, 600]
    ]

    objects2 = [
        [0, 0, 10, 190],
        [0, 420, 6, 600],
        [0, 0, 800, 90],
        [153, 90, 800, 159],
        [0, 534, 800, 600]
    ]

    objects3 = [
        [0, 0, 800, 159],
        [0, 534, 183, 600],
        [300, 530, 350, 600],
        [515, 534, 800, 600],
        [378, 0, 800, 168]
    ]

    objects4 = [
        [0, 0, 9, 600],
        [0, 0, 800, 85],
        [666, 0, 800, 600],
        [0, 590, 238, 600],
        [350, 590, 800, 600],
        [570, 0, 800, 230]
    ]


    if game_screen == 1:
        which_objects = objects
    elif game_screen == 2:
        which_objects = objects2
    elif game_screen == 3:
        which_objects = objects3
    elif game_screen == 4:
        which_objects = objects4
    for coordinates in which_objects:
        collision = False
        if player_position[0] >= coordinates[0] and player_position[1] >= coordinates[1] and player_position[0] <= coordinates[2] and player_position[1] <= coordinates[3]:
            collision = True
        if player_position[2] >= coordinates[0] and player_position[3] >= coordinates[1] and player_position[2] <= coordinates[2] and player_position[3] <= coordinates[3]:
            collision = True
        if player_position[4] >= coordinates[0] and player_position[5] >= coordinates[1] and player_position[4] <= coordinates[2] and player_position[5] <= coordinates[3]:
            collision = True
        if player_position[6] >= coordinates[0] and player_position[7] >= coordinates[1] and player_position[6] <= coordinates[2] and player_position[7] <= coordinates[3]:
            collision = True
        if player_position[8] >= coordinates[0] and player_position[9] >= coordinates[1] and player_position[8] <= coordinates[2] and player_position[9] <= coordinates[3]:
            collision = True
        if player_position[10] >= coordinates[0] and player_position[11] >= coordinates[1] and player_position[10] <= coordinates[2] and player_position[11] <= coordinates[3]:
            collision = True
        if player_position[12] >= coordinates[0] and player_position[13] >= coordinates[1] and player_position[12] <= coordinates[2] and player_position[13] <= coordinates[3]:
            collision = True
        if player_position[14] >= coordinates[0] and player_position[15] >= coordinates[1] and player_position[14] <= coordinates[2] and player_position[15] <= coordinates[3]:
            collision = True

        if collision:
            for cords in range(0, 16):
                player_position[cords] = player_position_before[cords]