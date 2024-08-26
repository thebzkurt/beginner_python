import random

word_list = ["apple","banana",]

random_word = random.choice(word_list)
print(random_word)

lives = len(random_word)
print(lives)

secret_word = ""
world_leng = len(random_word)

for positin in range(world_leng):
    secret_word += "-"
print(secret_word)

game_over = False
crrct_letters = []

while not game_over:
    print(f"your lives {lives}/{len(random_word)}")
    guess = input("Please guess a letter:  ").lower()
     
    if guess in crrct_letters:
        print(f"already guessed  *** {guess} ***")


    display = ""


    for letter in random_word:
        if letter == guess:
            display += guess
            crrct_letters.append(guess)
        elif letter in crrct_letters:
            display += letter
        else:
            display += "-"
    print(display)

    if guess  not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"your lives {lives}/{len(random_word)}")
            print("*************************************")
            print("lost")

    if "-" not in display:
        game_over = True
        print("*************************************")
        print("win")