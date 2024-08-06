import random


class guessing_game_class:
    def __init__(self):
        self.nbmr_list = list(range(1,101))
        self.guess_life = 5
        self.random_nmbr = random.choice(self.nbmr_list)


    def get_number(self):
        while True:
            try:
                number = int(input("Guess a number between 1 and 100: "))
                if number in self.nbmr_list:
                    if number == self.random_nmbr:
                        print(f"Your guess: {number} is correct. Computer number: {self.random_nmbr}. Your Win **!!**")
                    else:
                        self.guess_life -= 1
                        print(f"your right to guess 5/{self.guess_life}")
                        if self.guess_life == 0:
                            print(f"your right to guess is over. Computer number{self.random_nmbr}. Your lose **!!**")
                        else:
                            print(f"Your guess: {number} is wrong. Please try agin. :)" )
                else:
                    print("Number out of range. Please guess a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
       

game = guessing_game_class()
number, random_nmbr = game.get_number()

print("***********************************************")
print(f"Your guess: {number}, Random number: {random_nmbr}")
