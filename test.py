import random

class GuessingGame:
    def __init__(self):
        self.number_list = list(range(1, 11))
        self.guess_life = 5
        self.random_number = random.choice(self.number_list)

    def control(self, number):
        if number < self.random_number:
            print(f"Greater than {number}\n")
        elif number > self.random_number:
            print(f"Less than {number}\n")
        print("Please try again.\n")

    def get_number(self):
        while self.guess_life > 0:
            try:
                number = int(input("\nGuess a number between 1 and 10: "))
                if number in self.number_list:
                    if number == self.random_number:
                        print(f"\nYour guess: {number} is correct. Computer number: {self.random_number}. You Win **!!**")
                        break
                    else:
                        self.guess_life -= 1
                        print("---------------------------------------")
                        print(f"Your right to guess 5/{self.guess_life}")
                        if self.guess_life == 0:
                            print(f"\nYour right to guess is over. Computer number: {self.random_number}. You lose **!!**")
                        else:
                            self.control(number)
                else:
                    print("Number out of range. Please guess a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = GuessingGame()
    game.get_number()
    print("***********************************************")