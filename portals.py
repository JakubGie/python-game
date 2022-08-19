def teleportations(player_position, player_position_before, game_screen):
    from position import get_position
    global portals, portals2, portals3, portals4
    portals = [
        [670, 180, 750, 470, 2]
    ]

    portals2 = [
        [0, 180, 1, 470, 1],
        [798, 0, 800, 600, 3]
    ]

    portals3 = [
        [0, 0, 2, 600, 2],
        [430, 160, 485, 200, 4]
    ]

    portals4 = [
        [230, 598, 360, 600, 3]
    ]

    if game_screen == 1:
        which_portals = portals
    if game_screen == 2:
        which_portals = portals2
    if game_screen == 3:
        which_portals = portals3
    if game_screen == 4:
        which_portals = portals4
    for coordinates in which_portals:
        teleport = False
        if player_position[0] >= coordinates[0] and player_position[1] >= coordinates[1] and player_position[0] <= \
                coordinates[2] and player_position[1] <= coordinates[3]:
            teleport = True
        if player_position[2] >= coordinates[0] and player_position[3] >= coordinates[1] and player_position[2] <= \
                coordinates[2] and player_position[3] <= coordinates[3]:
            teleport = True
        if player_position[4] >= coordinates[0] and player_position[5] >= coordinates[1] and player_position[4] <= \
                coordinates[2] and player_position[5] <= coordinates[3]:
            teleport = True
        if player_position[6] >= coordinates[0] and player_position[7] >= coordinates[1] and player_position[6] <= \
                coordinates[2] and player_position[7] <= coordinates[3]:
            teleport = True
        if player_position[8] >= coordinates[0] and player_position[9] >= coordinates[1] and player_position[8] <= \
                coordinates[2] and player_position[9] <= coordinates[3]:
            teleport = True
        if player_position[10] >= coordinates[0] and player_position[11] >= coordinates[1] and player_position[10] <= \
                coordinates[2] and player_position[11] <= coordinates[3]:
            teleport = True
        if player_position[12] >= coordinates[0] and player_position[13] >= coordinates[1] and player_position[12] <= \
                coordinates[2] and player_position[13] <= coordinates[3]:
            teleport = True
        if player_position[14] >= coordinates[0] and player_position[15] >= coordinates[1] and player_position[14] <= \
                coordinates[2] and player_position[15] <= coordinates[3]:
            teleport = True

        if teleport:
            game_screen_before = game_screen
            game_screen = coordinates[4]

            if game_screen_before == 2 and game_screen == 1:
                get_position(600, player_position[1], player_position)
            elif game_screen_before == 1 and game_screen == 2:
                get_position(3, player_position[1], player_position)
            elif game_screen_before == 2 and game_screen == 3:
                get_position(3, player_position[1], player_position)
            elif game_screen_before == 3 and game_screen == 2:
                get_position(733, player_position[1], player_position)
            elif game_screen_before == 3 and game_screen == 4:
                get_position(261, 530, player_position)
            elif game_screen_before == 4 and game_screen == 3:
                get_position(430, 205, player_position)
            return game_screen


def monitoring(player_position, game_screen, screen, point):
    import pygame
    if game_screen == 1:
        for coordinates in portals:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (0, 0, 255), (coordinates[0], coordinates[1], width, height))
    if game_screen == 2:
        for coordinates in portals2:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (0, 0, 255), (coordinates[0], coordinates[1], width, height))
    if game_screen == 3:
        for coordinates in portals3:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (0, 0, 255), (coordinates[0], coordinates[1], width, height))
    if game_screen == 4:
        for coordinates in portals4:
            width = coordinates[2] - coordinates[0]
            height = coordinates[3] - coordinates[1]
            pygame.draw.rect(screen, (0, 0, 255), (coordinates[0], coordinates[1], width, height))