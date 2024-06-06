from Board import Board
from ai import AI
import time

WIDTH = 800
HEIGHT = 800
CELL_SIZE = WIDTH // 8


def setup():
    size(WIDTH, HEIGHT)
    global board
    light_color = color(255,222,173)
    dark_color = color(92, 64, 51)
    board = Board(WIDTH, HEIGHT, CELL_SIZE, light_color, dark_color)
    board.setup_checkers()
    global ai
    ai = AI("red", 1)  # Create an instance of the AI class
    ai.move_start_time = time.time()

def draw():
    board.draw_board()
    
def mousePressed():
    board.mouse_pressed()

def mouseReleased():
    board.mouse_released()
    
def mouseDragged():
    board.mouse_dragged()

def score(winner):
    # prompt user for name and update scores file
    name = input('Enter your name: ')
    scores = []
    with open('scores.txt', 'r') as f:
        for line in f:
            tokens = line.split()
            scores.append((tokens[0], int(tokens[1])))
    scores.append((name, 1))
    scores.sort(key=lambda x: x[1], reverse=True)
    with open('scores.txt', 'w') as f:
        for score in scores:
            f.write(score[0] + ' ' + str(score[1]) + '\n')
