import time

class AI:
    def __init__(self, color, delay_time):
        self.color = color
        self.delay_time = delay_time
        self.move_start_time = None
        self.ai_move_ready = False

    def computer_move(self, checkers):
        # Make red checker move and jump
        for i, c in enumerate(checkers):
            if c.valid_jump:
                checkers[i].x = c.jumps[0][0]
                checkers[i].y = c.jumps[0][1]
                checkers[i].board_x = self.HALF_SQUARE + checkers[i].x * self.SQUARE_SIZE
                checkers[i].board_y = self.HALF_SQUARE + checkers[i].y * self.SQUARE_SIZE
                return checkers

        for i, c in enumerate(checkers):
            if c.can_move:
                checkers[i].x = c.moves[0][0]
                checkers[i].y = c.moves[0][1]
                checkers[i].board_x = self.HALF_SQUARE + checkers[i].x * self.SQUARE_SIZE
                checkers[i].board_y = self.HALF_SQUARE + checkers[i].y * self.SQUARE_SIZE
                return checkers

        return checkers

    def is_move_ready(self):
        if self.move_start_time is None:
            return False
        elapsed_time = time.time() - self.move_start_time
        if elapsed_time >= self.delay_time:
            self.computer_move_ready = True
        return self.computer_move_ready

    def reset(self):
        self.move_start_time = None
        self.computer_move_ready = False
