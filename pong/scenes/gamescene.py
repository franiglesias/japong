import pygame

from pong.app.scene import Scene
from pong.app.window import Window


class GameScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        import pong.ball
        import pong.border
        import pong.config
        import pong.goal
        import pong.pad
        import pong.player
        import pong.scoreboard

        screen = self.window.screen
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
        self.window.score_board = pong.scoreboard.ScoreBoard(player1, player2)
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
            self.window.score_board.draw(self)
            all_sprites.draw(screen)

            # Screen update
            pygame.display.flip()

            if self.window.score_board.stop():
                done = True

            clock.tick(pong.config.FPS)

        return 0
