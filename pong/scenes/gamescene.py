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
        import pong.game.pad
        import pong.player
        import pong.scoreboard

        screen = self.window.screen
        # game loop control
        done = False
        # screen updates
        clock = pygame.time.Clock()
        ball = pong.ball.Ball(pong.config.yellow, 10)

        human_side = self.window.game.side_preference
        if human_side == 'left':
            computer_side = 'right'
        else:
            computer_side = 'left'

        human_player = pong.player.Player('human')
        human_pad = pong.game.pad.Pad(human_side, 2)

        computer_pad = pong.game.pad.Pad(computer_side)
        computer_player = pong.player.Player('computer')

        border_top = pong.border.Border(0)
        border_bottom = pong.border.Border(590)

        if human_side == 'left':
            goal_left = pong.goal.Goal(0, computer_player)
            goal_right = pong.goal.Goal(790, human_player)
            self.window.score_board = pong.scoreboard.ScoreBoard(human_player, computer_player)
        else:
            goal_left = pong.goal.Goal(0, human_player)
            goal_right = pong.goal.Goal(790, computer_player)
            self.window.score_board = pong.scoreboard.ScoreBoard(computer_player, human_player)

        # Prepare sprites
        all_sprites = pygame.sprite.Group()
        all_sprites.add(ball)
        all_sprites.add(border_top)
        all_sprites.add(border_bottom)
        all_sprites.add(goal_left)
        all_sprites.add(goal_right)
        all_sprites.add(human_pad)
        all_sprites.add(computer_pad)
        pads = pygame.sprite.Group()
        pads.add(human_pad)
        pads.add(computer_pad)
        borders = pygame.sprite.Group()
        borders.add(border_top)
        borders.add(border_bottom)
        ball.borders = borders
        human_pad.borders = borders
        computer_pad.borders = borders
        ball.pads = pads
        goals = pygame.sprite.Group()
        goals.add(goal_left)
        goals.add(goal_right)
        # Game loop

        pygame.time.set_timer(pong.config.COMPUTER_MOVES_EVENT, pong.config.COMPUTER_MOVES_TIMER_MS)
        while not done:
            # Event
            for event in pygame.event.get():
                if event.type == pong.config.COMPUTER_MOVES_EVENT:
                    computer_pad.follow(ball)
                if event.type == pygame.QUIT:
                    done = True

            # Game logic
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                human_pad.up()
            elif key[pygame.K_s]:
                human_pad.down()
            else:
                human_pad.stop()

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
