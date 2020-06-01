import pygame


def ponggame():
    import pong.ball
    import pong.border
    import pong.config
    import pong.goal
    import pong.pad
    import pong.player
    import pong.scoreboard

    # Prepare the screen
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ja pong!")
    # Prepare sound effects

    # game loop control
    done = False
    # screen updates
    clock = pygame.time.Clock()
    ball = pong.ball.Ball(pong.config.yellow, 10)
    pad_left = pong.pad.Pad('left')
    pad_right = pong.pad.Pad('right')
    pads = pygame.sprite.Group()
    pads.add(pad_left)
    pads.add(pad_right)
    border_top = pong.border.Border(0)
    border_bottom = pong.border.Border(590)
    player1 = pong.player.Player('left')
    player2 = pong.player.Player('computer')
    score_board = pong.scoreboard.ScoreBoard(player1, player2)
    goal_left = pong.goal.Goal(0, player2)
    goal_right = pong.goal.Goal(790, player1)
    # Prepare sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(ball)
    all_sprites.add(border_top)
    all_sprites.add(border_bottom)
    all_sprites.add(goal_left)
    all_sprites.add(goal_right)
    all_sprites.add(pad_left)
    all_sprites.add(pad_right)
    borders = pygame.sprite.Group()
    borders.add(border_top)
    borders.add(border_bottom)
    ball.borders = borders
    pad_left.borders = borders
    pad_right.borders = borders
    ball.pads = pads
    goals = pygame.sprite.Group()
    goals.add(goal_left)
    goals.add(goal_right)
    # Game loop
    while not done:
        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Game logic
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            pad_left.up()
        elif key[pygame.K_s]:
            pad_left.down()
        else:
            pad_left.stop()

        pad_right.follow(ball)

        all_sprites.update()

        # Manage collisions
        goal_collisions = pygame.sprite.spritecollide(ball, goals, False)
        for goal in goal_collisions:
            goal.hit()
            goal.player.point()
            ball.restart()

        # Game draw
        screen.fill(pong.config.green)
        score_board.draw(screen)
        all_sprites.draw(screen)

        # Screen update
        pygame.display.flip()

        if score_board.stop():
            done = True

        clock.tick(pong.config.FPS)

    scoreFont = pygame.font.Font(pygame.font.get_default_font(), 64)
    text = scoreFont.render('Game finished', True, pong.config.yellow, pong.config.green)
    score_board.winner(screen)
    text_rect = text.get_rect()
    text_rect.center = (800 // 2, 600 // 2)
    screen.blit(text, text_rect)
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
    pygame.quit()
