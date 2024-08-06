import random


class guessing_game_class:
    def __init__(self):
        self.nbmr_list = list(range(1,11))
        self.guess_life = 5
        self.random_nmbr = random.choice(self.nbmr_list)

    def control(self, number, random_nmbr):
        if number < random_nmbr:
            print(f"Greater than {number}\n")
            print("Please try agin.\n")
        elif number > random_nmbr:
            print(f"Less than {number}\n")
            print("Please try agin.\n")



    def get_number(self):
        while True:
            try:
                number = int(input("\nGuess a number between 1 and 10: "))
                if number in self.nbmr_list:
                    if number == self.random_nmbr:
                        return print(f"\nYour guess: {number} is correct. Computer number: {self.random_nmbr}. \nYour Win **!!**")
                    else:
                        self.guess_life -= 1
                        print("---------------------------------------")
                        print(f"your right to guess 5/{self.guess_life}")
                        if self.guess_life == 0:
                            return print(f"\nyour right to guess is over. Computer number: {self.random_nmbr}. \nYour lose **!!**")
                        else:
                            a = guessing_game_class()
                            a.control(number=number, random_nmbr=self.random_nmbr)
                            print(self.random_nmbr)
                            #print(f"Your guess: {number} is wrong. Please try agin. :)" )
                else:
                    print("Number out of range. Please guess a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
       

game = guessing_game_class()
random_nmbr = game.get_number()

print("***********************************************")
#=print(f"Your guess: {self.number}, Random number: {random_nmbr}")
