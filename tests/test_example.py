import os
import sys

# Add src to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from example import WordGame


def test_initial_display():
    """Test initial display: '_ _ _ _ _'"""
    # Assuming the game initializes with a secret word "apple"
    # and display should show underscores for each letter separated by space
    game = WordGame("apple")
    assert game.display() == "_ _ _ _ _"


def test_correct_guess_updates_display():
    """Test correct guess updates display"""
    game = WordGame("apple")
    game.guess("a")
    # 'a' is revealed
    assert game.display() == "a _ _ _ _"

    game.guess("p")
    # Both 'p's should be revealed
    assert game.display() == "a p p _ _"


def test_incorrect_guess_decrements_attempts():
    """Test incorrect guess decrements attempts"""
    game = WordGame("apple", max_attempts=5)
    initial_count = game.guess_count

    # 'z' is not in 'apple'
    game.guess("z")

    # guess_count should increase (attempts used)
    assert game.guess_count == initial_count + 1

    # # If get_hangman_status exists, it should show 4 attempts left
    # if hasattr(game, "get_hangman_status"):
    #     assert game.get_hangman_status() == 4


def test_duplicate_guess_no_penalty():
    """Failing: Duplicate guess returns False, no decrement"""
    game = WordGame("apple")

    # First correct guess
    assert game.guess("a") is True
    first_count = game.guess_count

    # Duplicate correct guess
    assert game.guess("a") is False
    assert game.guess_count == first_count

    # First incorrect guess
    game.guess("z")
    second_count = game.guess_count
    assert game.guess_count == 2

    # Duplicate incorrect guess
    assert game.guess("z") is False
    assert game.guess_count == 2
    # This is currently failing in implementation (incorrect guesses aren't tracked)
    assert game.guess_count == second_count


def test_case_insensitivity():
    """Failing: Case insensitivity"""
    # Init with mixed case
    game = WordGame("Apple")

    # Guess with different case
    assert game.guess("a") is True
    # Guess uppercase for a lowercase in word
    assert game.guess("P") is True
    assert "p" in game.guessed_letters


def test_is_won():
    """Failing: is_won() after all letters guessed"""
    game = WordGame("hi")
    assert not game.is_won()

    game.guess("h")
    assert not game.is_won()

    game.guess("i")
    assert game.is_won()


def test_get_hangman_status():
    """Extend: Add get_hangman_status() returning attempts left"""
    game = WordGame("apple", max_attempts=6)

    # Should exist and return max_attempts initially
    assert hasattr(game, "get_hangman_status")
    assert game.get_hangman_status() == 6

    game.guess("z")
    assert game.get_hangman_status() == 5
