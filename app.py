import pygame, collisions, portals, position

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("III Miecze")
icon = pygame.image.load("assets/player/head.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

menu_image = pygame.image.load("assets/menu.png")

screen_image = pygame.image.load("assets/screens/screen.jpg")
screen2_image = pygame.image.load("assets/screens/screen2.jpg")
screen2on_image = pygame.image.load("assets/screens/screen2on.png")
screen3_image = pygame.image.load("assets/screens/screen3.jpg")
screen3on_image = pygame.image.load("assets/screens/screen3on.png")
screen4_image = pygame.image.load("assets/screens/screen4.jpg")
end_screen_image = pygame.image.load("assets/screens/end.jpg")

dialogue_image = pygame.image.load("assets/dialogue.png")

point = pygame.image.load("assets/point.png")

villager_image = pygame.image.load("assets/characters/villager.png")
musician_image = pygame.image.load("assets/characters/musician.png")
blacksmith_image = pygame.image.load("assets/characters/blacksmith.png")

sword_image = pygame.image.load("assets/sword.png")

player_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
player_position_before = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def player(x, y):
    screen.blit(player_image, (x, y))

playerX = ""
walkingX_before = "right"

def player_walking():
    global player_image
    if walkingX == "no" and walkingY == "no":
        if walkingX_before == "left":
            player_image = pygame.image.load('assets/player/player-left.png')
        else:
            player_image = pygame.image.load('assets/player/player.png')
    if walkingX == "left":
        player_image = pygame.image.load('assets/player/player-left.png')
    if walkingX == "right":
        player_image = pygame.image.load('assets/player/player.png')
    if walkingY == "up" and playerX == "right":
        player_image = pygame.image.load('assets/player/player.png')
    if walkingY == "up" and playerX == "left":
        player_image = pygame.image.load('assets/player/player-left.png')
    if walkingY == "down" and playerX == "left":
        player_image = pygame.image.load('assets/player/player-left.png')

issound = False

sound_number = 0

def sounds(sound_number_in):
    global issound, sound_number
    if sound_number_in != sound_number:
        pygame.mixer.music.fadeout(1300)
    sound_number = sound_number_in
    if sound_number != 0:
        sound_number = sound_number_in
    if not issound:
        if sound_number == 1:
            pygame.mixer.music.load("assets/sounds/music.mp3")
            pygame.mixer_music.play(loops=9999)
            issound = True
        if sound_number == 2:
            pygame.mixer.music.load("assets/sounds/music2.mp3")
            pygame.mixer_music.play(loops=9999)
            issound = True
        if sound_number == 3:
            pygame.mixer.music.load("assets/sounds/endmusic.mp3")
            pygame.mixer_music.play()
            issound = True


def dialogue(text, x, y, font_size):
    screen.blit(dialogue_image, (0, 530))
    font_dialogue = pygame.font.Font('assets/fonts/OldStandardTT-Regular.ttf', font_size)
    textsurface = font_dialogue.render(text, False, (255, 255, 255))
    screen.blit(textsurface, (x, y))

is_dialogue = False
dialogue_parts = ["", 0, 0, 0]

character_position = [0, 0]
which_frame = 1
which_frame2 = 1

fields = [
        [500, 30, 600, 100, 1, False]
    ]

fields2 = [
    [600, 0, 630, 600, 1, True]
]

fields3 = [
    [300, 0, 350, 600, 1, True],
    [430, 160, 485, 230, 2, False]
]

fields4 = [
    [520, 0, 570, 280, 1, True],
    [510, 0, 580, 298, 2, False]
]

wait_point = 0
def wait(time):
    global wait_point
    wait_point += 1
    wait_point_secs = wait_point / 60
    if wait_point_secs == time:
        wait_point = 0
        return "now"
    else:
        return "not yet"

after_wait = False
next_dialogue = False
sword_searching = False
ending = False
end_walking = False
end_sound = False

def detections(player_position, player_position_before, game_screen):
    global speedX, speedY, walkingX, character_position, which_frame, is_dialogue, dialogue_parts, after_wait, wait_point, next_dialogue, sword_searching, how_many_swords, ending, end_walking, issound, end_sound, end, game, which_frame2

    if game_screen == 1:
        which_fields = fields
    if game_screen == 2:
        which_fields = fields2
    if game_screen == 3:
        which_fields = fields3
    if game_screen == 4:
        which_fields = fields4
    for coordinates in which_fields:
        detect = False
        if player_position[0] >= coordinates[0] and player_position[1] >= coordinates[1] and player_position[0] <= \
                coordinates[2] and player_position[1] <= coordinates[3]:
            detect = True
        if player_position[2] >= coordinates[0] and player_position[3] >= coordinates[1] and player_position[2] <= \
                coordinates[2] and player_position[3] <= coordinates[3]:
            detect = True
        if player_position[4] >= coordinates[0] and player_position[5] >= coordinates[1] and player_position[4] <= \
                coordinates[2] and player_position[5] <= coordinates[3]:
            detect = True
        if player_position[6] >= coordinates[0] and player_position[7] >= coordinates[1] and player_position[6] <= \
                coordinates[2] and player_position[7] <= coordinates[3]:
            detect = True
        if player_position[8] >= coordinates[0] and player_position[9] >= coordinates[1] and player_position[8] <= \
                coordinates[2] and player_position[9] <= coordinates[3]:
            detect = True
        if player_position[10] >= coordinates[0] and player_position[11] >= coordinates[1] and player_position[10] <= \
                coordinates[2] and player_position[11] <= coordinates[3]:
            detect = True
        if player_position[12] >= coordinates[0] and player_position[13] >= coordinates[1] and player_position[12] <= \
                coordinates[2] and player_position[13] <= coordinates[3]:
            detect = True
        if player_position[14] >= coordinates[0] and player_position[15] >= coordinates[1] and player_position[14] <= \
                coordinates[2] and player_position[15] <= coordinates[3]:
            detect = True

        if detect:
            if which_fields == fields2 and coordinates[5] == True and coordinates[4] == 1:
                speedX = 0
                speedY = 0
                walkingX = "left"

                is_dialogue = True
                dialogue_parts = ["Hej, ty!", 350, 545, 30]

                if character_position[1] != player_position[1] and character_position[1] != player_position[1] + 1 and after_wait == False:
                    if which_frame == 1:
                        character_position = [44, 78]
                    else:
                        character_position[1] += 2
                else:
                    if character_position[0] != player_position[0]-100 and character_position[0] != player_position[0]-101 and after_wait == False:
                        character_position[0] += 2
                    else:
                        is_dialogue = False
                        is_dialogue = True
                        dialogue_parts = ["Kowal cię szukał, ma dla ciebie jakieś zlecenie", 106, 545, 30]
                        if wait(6.5) == "now":
                            after_wait = True
                        if after_wait:
                            is_dialogue = False
                            if character_position[0] != 44 and character_position[0] != 45:
                                character_position[0] -= 2
                            else:
                                if character_position[1] != 77 and character_position[1] != 78:
                                    character_position[1] -= 2
                                else:
                                    coordinates[5] = False
                                    after_wait = False
                                    wait_point = 0
                screen.blit(villager_image, (character_position))

                which_frame += 1
            if which_fields == fields3 and coordinates[5] == True and coordinates[4] == 1:
                speedX = 0
                speedY = 0
                is_dialogue = True
                dialogue_parts = ["Ci grajkowie, powinni wziąć szable i walczyć!", 100, 545, 30]
                if wait(6.5) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    coordinates[5] = False
                    after_wait = False
                    wait_point = 0
            if which_fields == fields4 and coordinates[5] == True and coordinates[4] == 1:
                speedX = 0
                speedY = 0
                is_dialogue = True
                walkingX = "right"
                dialogue_parts = ["Dobrze, że jesteś! Mam dla ciebie robotę", 130, 545, 30]
                if wait(6) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    next_dialogue = True
                    coordinates[5] = False
                    after_wait = False
                    wait_point = 0
            if which_fields == fields4 and coordinates[5] == False and coordinates[4] == 1 and next_dialogue:
                speedX = 0
                speedY = 0
                is_dialogue = True
                dialogue_parts = ["Zniknęły mi trzy miecze, znajdź je!", 160, 545, 30]
                walkingX = "right"
                if wait(8) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    after_wait = False
                    next_dialogue = False
                    wait_point = 0
                    sword_searching = True
                    for coordinates2 in fields3:
                        if coordinates2[4] == 2:
                            coordinates2[5] = True
            if which_fields == fields3 and coordinates[5] == True and coordinates[4] == 2:
                speedX = 0
                speedY = 0
                is_dialogue = True
                dialogue_parts = ["Podobno na terenie przed królestwem widziano porzucone miecze", 63, 548, 24]
                if wait(8) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    coordinates[5] = False
                    after_wait = False
                    wait_point = 0
                    for coordinates2 in fields:
                        if coordinates2[4] == 1:
                            coordinates2[5] = True
            if which_fields == fields and coordinates[5] == True and coordinates[4] == 1:
                speedX = 0
                speedY = 0
                is_dialogue = True
                dialogue_parts = ["Są i miecze, niestety jest ich tylko dwa", 130, 545, 30]
                if wait(6.5) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    next_dialogue = True
                    coordinates[5] = False
                    after_wait = False
                    wait_point = 0
            if which_fields == fields and coordinates[5] == False and coordinates[4] == 1 and next_dialogue:
                speedX = 0
                speedY = 0
                is_dialogue = True
                dialogue_parts = ["Powinienem zanieść je do kowala", 170, 545, 30]
                if wait(8.5) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    after_wait = False
                    next_dialogue = False
                    wait_point = 0
                    how_many_swords = 2
                    for coordinates2 in fields4:
                        if coordinates2[4] == 2:
                            coordinates2[5] = True
                    ending = True
            if which_fields == fields4 and coordinates[5] == True and coordinates[4] == 2:
                if sound_number != 3:
                    issound = False
                    sounds(3)
                end_sound = True
                speedX = 0
                speedY = 0
                is_dialogue = True
                walkingX = "right"
                dialogue_parts = ["Udało mi się znaleźć tylko dwa miecze, ale jako trzeci oddam ci mój miecz", 56, 550, 22]
                if wait(10) == "now":
                    after_wait = True
                if after_wait:
                    is_dialogue = False
                    next_dialogue = True
                    coordinates[5] = False
                    after_wait = False
                    wait_point = 0
            if which_fields == fields4 and coordinates[5] == False and coordinates[4] == 2 and next_dialogue and ending:
                how_many_swords = 3
                speedX = 0
                speedY = 0
                if end_walking == False:
                    is_dialogue = True
                    dialogue_parts = ["Postanowiłem zmienić swoje życie, zostanę grajkiem!", 60, 545, 30]
                walkingX = "right"
                if wait(8) == "now":
                    after_wait = True
                if after_wait:
                    if which_frame2 == 1:
                        player_position[0] = 450
                        player_position[1] = 230
                    which_frame2 +=1
                    is_dialogue = False
                    if player_position[0] != 247 and player_position[0] != 248:
                        player_position[0] -= 2
                    else:
                        end_walking = True
                        coordinates[5] = False
                        wait_point = 0
                        if player_position[1] != 530 and player_position[1] != 531:
                            player_position[1] += 2
                        else:
                            sword_searching = False
                            end = True
                            game = False
                            after_wait = False
                            wait_point = 0


        else:
            which_frame = 1

def monitoring(player_position, game_screen, screen, point):
    if game_screen == 1:
        for coordinates in fields:
            if coordinates[5] == True:
                width = coordinates[2] - coordinates[0]
                height = coordinates[3] - coordinates[1]
                pygame.draw.rect(screen, (0, 255, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 2:
        for coordinates in fields2:
            if coordinates[5] == True:
                width = coordinates[2] - coordinates[0]
                height = coordinates[3] - coordinates[1]
                pygame.draw.rect(screen, (0, 255, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 3:
        for coordinates in fields3:
            if coordinates[5] == True:
                width = coordinates[2] - coordinates[0]
                height = coordinates[3] - coordinates[1]
                pygame.draw.rect(screen, (0, 255, 0), (coordinates[0], coordinates[1], width, height))
    if game_screen == 4:
        for coordinates in fields4:
            if coordinates[5] == True:
                width = coordinates[2] - coordinates[0]
                height = coordinates[3] - coordinates[1]
                pygame.draw.rect(screen, (0, 255, 0), (coordinates[0], coordinates[1], width, height))


speedX = 0
speedY = 0

font = pygame.font.Font('assets/fonts/OldStandardTT-Bold.ttf', 100)
font2 = pygame.font.Font('assets/fonts/OldStandardTT-Regular.ttf', 30)
font3 = pygame.font.Font('assets/fonts/OldStandardTT-Regular.ttf', 40)
font4 = pygame.font.Font('assets/fonts/OldStandardTT-Regular.ttf', 28)

running = True
game = False
start = True
end = False
game_screen = 1
walkingX = "no"
walkingY = "no"

position.get_position(60, 188, player_position)

endX = 450
endY = 170

how_many_swords = 0
all_swords = 3

while running:
    if end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_image = pygame.image.load('assets/player/player-left.png')
        screen.blit(end_screen_image, (0, 0))
        screen.blit(player_image, (endX, endY))
        if endY != 370 and endY != 371:
            endY +=2
        else:
            if endX != 130 and endX != 131:
                endX -= 2
            else:
                screen.blit(menu_image, (0, 0))
                textsurface = font.render('III Miecze', False, (255, 255, 255))
                screen.blit(textsurface, (164, 260))
                if wait(2.1) == "now":
                    after_wait = True
                if after_wait:
                    screen.blit(menu_image, (0, 0))
                    textsurface = font.render('By Kolberg', False, (255, 255, 255))
                    screen.blit(textsurface, (125, 260))
    else:
        if start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= 150 and event.pos[0] <= 630 and event.pos[1] >= 350 and event.pos[1] <= 450:
                        start = False
                        game = True

            if sound_number != 2:
                issound = False
            sounds(2)

            screen.blit(menu_image, (0, 0))
            textsurface = font.render('III Miecze', False, (255, 255, 255))
            screen.blit(textsurface, (164, 100))
            textsurface = font2.render('„Kto mieczem wojuje, ten od miecza ginie”', False, (255, 255, 255))
            screen.blit(textsurface, (120, 230))

            pygame.draw.rect(screen, (255, 255, 255), (150, 350, 480, 100))

            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] >= 150 and mouse_position[0] <= 630 and mouse_position[1] >= 350 and mouse_position[
                1] <= 450:
                pygame.draw.rect(screen, (204, 204, 204), (150, 350, 480, 100))

            textsurface = font3.render('Rozpocznij grę', False, (0, 0, 0))
            screen.blit(textsurface, (260, 380))
        else:
            if not game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[0] >= 150 and event.pos[0] <= 630 and event.pos[1] >= 350 and event.pos[1] <= 450:
                            game = True

                screen.blit(menu_image, (0, 0))
                textsurface = font.render('III Miecze', False, (255, 255, 255))
                screen.blit(textsurface, (164, 170))

                pygame.draw.rect(screen, (255, 255, 255), (150, 350, 480, 100))

                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] >= 150 and mouse_position[0] <= 630 and mouse_position[1] >= 350 and \
                        mouse_position[
                            1] <= 450:
                    pygame.draw.rect(screen, (204, 204, 204), (150, 350, 480, 100))

                textsurface = font3.render('Graj', False, (0, 0, 0))
                screen.blit(textsurface, (350, 383))


            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            speedX = -1
                            walkingX = "left"
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            speedX = 1
                            walkingX = "right"
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            speedY = -1
                            walkingY = "up"
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            speedY = 1
                            walkingY = "down"
                        if event.key == pygame.K_a:
                            speedX = -1
                        if event.key == pygame.K_ESCAPE and end_sound != True:
                            game = False
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                            speedX = 0
                            walkingX_before = walkingX
                            walkingX = "no"
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                            speedY = 0
                            walkingY = "no"

                if sound_number != 1 and end_sound!=True:
                    issound = False
                if end_sound!=True:
                    sounds(1)

                for cords in range(0, 16):
                    player_position_before[cords] = player_position[cords]


                if game_screen == 1:
                    screen.blit(screen_image, (0, 0))

                elif game_screen == 2:
                    screen.blit(screen2_image, (0, 0))

                elif game_screen == 3:
                    screen.blit(screen3_image, (0, 0))

                elif game_screen == 4:
                    screen.blit(screen4_image, (0, 0))



                detections(player_position, player_position_before, game_screen)


                for cords in range(0, 16):
                    if cords == 0 or cords % 2 == 0:
                        player_position[cords] += speedX
                    else:
                        player_position[cords] += speedY

                collisions.wall(player_position, player_position_before)
                collisions.collision(player_position, player_position_before, game_screen)
                portal = portals.teleportations(player_position, player_position_before, game_screen)
                if portal != None:
                    game_screen = portal

                player_walking()




                #collisions.monitoring(player_position, game_screen, screen, point)
                #portals.monitoring(player_position, game_screen, screen, point)
                #monitoring(player_position, game_screen, screen, point)


                player(player_position[0], player_position[1])

                if game_screen == 1:
                    textsurface = font4.render('Teren przed królestwem', False, (255, 255, 255))
                    screen.blit(textsurface, (10, 10))

                elif game_screen == 2:
                    textsurface = font4.render('Królestwo', False, (255, 255, 255))
                    screen.blit(textsurface, (10, 10))
                    screen.blit(screen2on_image, (0, 0))

                elif game_screen == 3:
                    textsurface = font4.render('Królestwo', False, (255, 255, 255))
                    screen.blit(textsurface, (10, 10))
                    screen.blit(screen3on_image, (0, 0))
                    screen.blit(musician_image, (300, 490))

                if game_screen == 4:
                    textsurface = font4.render('Kuźnia', False, (255, 255, 255))
                    screen.blit(textsurface, (10, 10))
                    screen.blit(blacksmith_image, (570, 160))



                if sword_searching:
                    text = f'{how_many_swords}/{all_swords}'
                    textsurface = font4.render(text, False, (255, 255, 255))
                    screen.blit(textsurface, (743, 14))
                    screen.blit(sword_image, (703, 10))
                    if how_many_swords!=2 and game_screen==1:
                        screen.blit(sword_image, (525, 50))
                        screen.blit(sword_image, (545, 50))


                if is_dialogue:
                    dg_text = dialogue_parts[0]
                    dg_x = dialogue_parts[1]
                    dg_y = dialogue_parts[2]
                    dg_font = dialogue_parts[3]
                    dialogue(dg_text, dg_x, dg_y, dg_font)

    clock.tick(120)

    pygame.display.update()