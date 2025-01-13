import random

class Lotto:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        self.numbers = random.sample(range(1, 46), 6)
        self.numbers.sort()
        return self.numbers

    def play(self):
        try:
            print(self.generate_numbers())
        except Exception as e:
            print("오류 발생:", e)

lotto_game = Lotto()
lotto_game.play()