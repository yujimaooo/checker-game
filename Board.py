import time
from checker import Checker
from ai import AI

class Board:
    def __init__(self, WIDTH, HEIGHT, CELL_SIZE, light_color, dark_color):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL_SIZE = CELL_SIZE
        self.light_color = light_color
        self.dark_color = dark_color
        self.checkers = []
        self.dragged_checker = None
        self.orig_x = 0
        self.orig_y = 0
        self.ai = AI(Color(255,0,0), 1) # Create an instance of the AI class with a red checker and a delay time of 1 second

    def setup_checkers(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.checkers.append(Checker(j, i, color(255,0,0)))
                    elif i > 4:
                        self.checkers.append(Checker(j, i, color(0)))

    def draw_board(self):
        for i in range(self.WIDTH // self.CELL_SIZE):
            for j in range(self.HEIGHT // self.CELL_SIZE):
                fill(self.light_color if (i + j) % 2 == 0 else self.dark_color)
                square(j * self.CELL_SIZE, i * self.CELL_SIZE, self.CELL_SIZE)

        for checker in self.checkers:
            if checker is not self.dragged_checker:
                checker.display(self.CELL_SIZE)

        if self.dragged_checker:
            self.dragged_checker.draw_at(mouseX, mouseY, self.CELL_SIZE)

    def mouse_pressed(self):
        for checker in self.checkers:
            if checker.is_mouse_over(mouseX, mouseY, self.CELL_SIZE):
                self.dragged_checker = checker
                self.orig_x, self.orig_y = checker.x, checker.y
                return

    def mouse_released(self):
        if self.dragged_checker:
            new_x = int(mouseX / self.CELL_SIZE)
            new_y = int(mouseY / self.CELL_SIZE)

            if self.dragged_checker.valid_move(new_x, new_y):
                self.dragged_checker.move(new_x, new_y, self.checkers)
                # Check if it's the AI's turn
                if self.dragged_checker.color == self.ai.color:
                    self.ai.move_start_time = time.time() # Start the timer for the AI move
                    ai = self.ai.computer_move(self.checkers)
            else:
                self.dragged_checker.move(self.orig_x, self.orig_y, self.checkers)
            self.dragged_checker = None

    def mouse_dragged(self):
        if self.dragged_checker:
            new_x = int(mouseX / self.CELL_SIZE)
            new_y = int(mouseY / self.CELL_SIZE)
