"""
for each guess:
  convert to lowercase
  if guess in guesses:
    # don't penalize
    return False
  increment guess-count
  if guess-count > max:
    throw Exception('fail')
  if guess in secret-word:
    add guess to guesses
    check if is-won
"""


class WordGame:
    def __init__(self, secret_word: str, max_attempts: int = 6):
        self.secret_word = secret_word.lower()
        self.max_attempts = max_attempts
        self.guess_count = 0
        self.guessed_letters = set()
        self.current_state = " ".join(["_"] * len(secret_word))
        # TODO: Add display logic

    def guess(self, letter: str) -> bool:
        letter = letter.lower()
        if letter in self.guessed_letters:
            # don't penalize
            return False
        self.guessed_letters.add(letter)
        self.guess_count += 1
        if self.guess_count > self.max_attempts:
            raise Exception("fail")
        if letter in self.secret_word:
            self.update(letter)
            self.is_won()
            return True
        return False

    def update(self, letter):
        arr = ["_"] * len(self.secret_word)
        for i, g in enumerate(self.secret_word):
            for ltr in self.guessed_letters:
                if ltr == g:
                    arr[i] = g
        self.current_state = " ".join(arr)

    def display(self) -> str:
        # TODO: Return current state like "_ e l l _"
        return self.current_state

    def is_won(self) -> bool:
        return self.current_state == " ".join(self.secret_word)

    def is_lost(self) -> bool:
        return self.guess_count >= self.max_attempts
