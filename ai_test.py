import time
from ai import AI

def setUp(self):
    self.ai = AI("red", 0.5)

def test_computer_move(self):
    ai = AI("red", 0.5)
    checkers = [
        Checker(1, 2, "black"),
        Checker(3, 4, "red", can_move=True),
        Checker(5, 6, "black", valid_jump=True, jumps=[(4, 5), (2, 3)]),
    ]
    
    result = ai.computer_move(checkers)

    expected_result = [
        Checker(1, 2, "black"),
        Checker(4, 5, "red", can_move=True, moves=[(3, 4)]),
        Checker(5, 6, "black", valid_jump=True, jumps=[(4, 5), (2, 3)]),
    ]
        
    assert result == expected_result

def test_is_move_ready(self):
    assert self.ai.is_move_ready() == False

    self.ai.move_start_time = time.time() - 3.0
    assert self.ai.is_move_ready() == False

    self.ai.move_start_time = time.time() - 2.0
    assert self.ai.is_move_ready() == True


def test_reset(self):
    self.ai.move_start_time = time.time() - 2.0
    self.ai.computer_move_ready = True
    self.ai.reset()
    assert self.ai.move_start_time == None
    assert self.ai.computer_move_ready == False

