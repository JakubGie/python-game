def get_position(x, y, player_position):
    player_position[0] = x
    player_position[1] = y
    for cords in range(2, 9):
        if cords == 2:
            player_position[2] = player_position[0] + 32
            player_position[3] = player_position[1]
        elif cords == 3:
            player_position[4] = player_position[2] + 32
            player_position[5] = player_position[3]
        elif cords == 4:
            player_position[6] = player_position[4]
            player_position[7] = player_position[5] + 32
        elif cords == 5:
            player_position[8] = player_position[6]
            player_position[9] = player_position[7] + 32
        elif cords == 6:
            player_position[10] = player_position[8] - 32
            player_position[11] = player_position[9]
        elif cords == 7:
            player_position[12] = player_position[10] - 32
            player_position[13] = player_position[11]
        elif cords == 8:
            player_position[14] = player_position[12]
            player_position[15] = player_position[13] - 32