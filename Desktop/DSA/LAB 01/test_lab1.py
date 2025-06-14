# IMPORT THE MODULE TO BE TESTED
import lab1_unique_fixed as lab1

# TEST THE FACTORIAL FUNCTION
def test_factorial():
    assert lab1.factorial(5) == 120
    assert lab1.factorial(0) == 1

# TEST THE FIBONACCI FUNCTION
def test_fibonacci():
    assert lab1.Fibonacci(7) == 13
    assert lab1.Fibonacci(0) == 0

# TEST THE SUM_TO_GOAL FUNCTION
def test_sum_to_goal():
    assert lab1.sum_to_goal([1, 2, 3, 4], 5) == 6
    assert lab1.sum_to_goal([1, 2, 3], 10) == 0

# TEST THE ROCK PAPER SCISSORS FUNCTION
def test_wins_rock_scissors_paper():
    assert lab1.wins_rock_scissors_paper("Rock", "Scissors") == True
    assert lab1.wins_rock_scissors_paper("Rock", "Rock") == False

# TEST THE INCREMENTER CLASS
def test_incrementer():
    inc = lab1.Incrementer(2)
    inc.update()
    inc.update()
    assert inc.count() == 4

# TEST THE DECREMENTER CLASS
def test_decrementer():
    dec = lab1.Decrementer(2)
    dec.update()
    dec.update()
    assert dec.count() == -4
