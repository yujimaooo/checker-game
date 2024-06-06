import math

class Checker:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.king = False
        self.img = loadImage("crown.png")
        self.jumps = [] 

    def display(self, CELL_SIZE):
        x = self.x * CELL_SIZE + CELL_SIZE // 2
        y = self.y * CELL_SIZE + CELL_SIZE // 2
        self.draw_at(x, y, CELL_SIZE)

    def draw_at(self, x, y, CELL_SIZE):
        stroke(255)
        strokeWeight(3)
        if self.is_mouse_over(mouseX, mouseY, CELL_SIZE):
            strokeWeight(5)
        fill(self.color)
        ellipse(x, y, CELL_SIZE * 0.8, CELL_SIZE * 0.8)
        strokeWeight(3)
        noFill()
        stroke(255)
        ellipse(x, y, CELL_SIZE * 0.6, CELL_SIZE * 0.6)

        strokeWeight(0)
        if self.king:
            fill(255)
            imageMode(CENTER)
            img = self.image
            image(img, x, y - 3, 50, 50)

    def move(self, x, y, board):
        if self.valid_move(x, y):
            self.x = x
            self.y = y
            if (self.color == color(255,0,0) and y == 7) or (self.color == color(0) and y == 0):
                self.king = True
        elif self.can_capture_to(x, y, board):
            board.capture(self, x, y)

    def is_mouse_over(self, mx, my, CELL_SIZE):
        dist_x = mx - self.x * CELL_SIZE - CELL_SIZE // 2
        dist_y = my - self.y * CELL_SIZE - CELL_SIZE // 2
        return math.sqrt(dist_x**2 + dist_y**2) < CELL_SIZE * 0.4

    def valid_move(self, new_x, new_y):
        moves = []
        if self.king:
            return abs(new_y - self.y) == 1
        else:
            if self.color == color(255, 0, 0):  # Moving downwards
                return new_y - self.y == 1 and abs(new_x - self.x) == 1
            else:  # Moving upwards
                return new_y - self.y == -1 and abs(new_x - self.x) == 1
    
    def valid_jump(self, board):
        jumps = []
        if self.king:
            # Check for jumps in all directions
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    if self._can_capture_in_direction(dx, dy, board):
                        jumps.append((self.x + 2*dx, self.y + 2*dy))
        else:
            # Check for jumps in the two directions allowed for this color
            for dy in [1, -1]:
                for dx in [-1, 1]:
                    if self._can_capture_in_direction(dx, dy, board):
                        jumps.append((self.x + 2*dx, self.y + 2*dy))
        return jumps

    def can_capture(self, new_x, new_y, board):
        if self.king:
            return self._can_capture_in_any_direction(new_x, new_y, board)
        else:
            if self.color == color(255, 0, 0):  # Moving downwards
                if new_y - int(self.y) == 2 and abs(new_x - int(self.x)) == 2:
                    mid_x = (int(self.x) + new_x) // 2
                    mid_y = (int(self.y) + new_y) // 2
                    for checker in board.checkers:
                        if checker.x == mid_x and checker.y == mid_y and checker.color != self.color:
                            # Check if the landing square is empty
                            landing_square = board.get_checker(new_x, new_y)
                            if landing_square is None:
                                return True
                            else:
                                return False
            else:  # Moving upwards
                if new_y - int(self.y) == -2 and abs(new_x - int(self.x)) == 2:
                    mid_x = (int(self.x) + new_x) // 2
                    mid_y = (int(self.y) + new_y) // 2
                    for checker in board.checkers:
                        if checker.x == mid_x and checker.y == mid_y and checker.color != self.color:
                            # Check if the landing square is empty
                            landing_square = board.get_checker(new_x, new_y)
                            if landing_square is None:
                                return True
                            else:
                                return False
        return False
