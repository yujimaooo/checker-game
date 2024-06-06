from checker import Checker
from Board import Board

WIDTH = 800
HEIGHT = 800
CELL_SIZE = 100
light_color = (255, 255, 255)
dark_color = (0, 0, 0)
board = Board(WIDTH, HEIGHT, CELL_SIZE, light_color, dark_color)


def test_move():
    checker = Checker(0, 0, "black")
    checker.move(1, 1)
    assert checker.x == 1
    assert checker.y == 1
    assert not checker.king
    checker.move(2, 2)
    assert checker.x == 2
    assert checker.y == 2


def test_is_mouse_over():
    checker = Checker(3, 4, "red")
    assert checker.is_mouse_over(175, 225, 50)  # inside the board
    assert not checker.is_mouse_over(100, 100, 50)  # outside the board


def test_valid_move():
    # Test valid moves for black checker
    black_checker = Checker(0, 0, "black")
    assert black_checker.valid_move(1, 1)
    assert not black_checker.valid_move(2, 1)
    
    # Test valid moves for red checker
    red_checker = Checker(3, 3, "red")
    assert red_checker.valid_move(2, 4)
    assert not red_checker.valid_move(3, 2)

def test_can_capture():
    # Test capture for black checker
    board = Board()
    black_checker = Checker(1, 1, "black")
    red_checker = Checker(2, 2, "red")
    board.checkers = [black_checker, red_checker]
    assert black_checker.can_capture(3, 3, board)
    assert not black_checker.can_capture(2, 2, board)
    
    # Test capture for red checker
    board = Board()
    red_checker = Checker(3, 3, "red")
    black_checker = Checker(2, 2, "black")
    board.checkers = [red_checker, black_checker]
    assert red_checker.can_capture(1, 1, board)
    assert not red_checker.can_capture(2, 2, board)
