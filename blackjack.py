import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
chek_list = ["hit","stand"]

#list
ia_list = []
ia_list_secret = ["*"]
player_list = []

player_num = 0
ia_num = 0

def adding(user,list):
    pass

def numdef(user,list):
    for numbers in list:
        user += numbers
    pass

#baslancig noktasi 2 tane random sayi aliniyor 
beginning = True
while beginning:

    random_ia = random.choice(cards)
    ia_list.append(random_ia)
    random_player = random.choice(cards)
    player_list.append(random_player)
    if 2 == len(ia_list) and 2 == len(player_list):
        beginning = False

#alinan random sayilari toplan alan ve bunlarin ciktida gozlenmesini saglayan diger kodlar
for numbers in player_list:
    player_num += numbers

for numbers in ia_list:
    ia_num += numbers

print(f"Computer cards: \n{ia_list}  num = {ia_num}")
print(f"Your cards: \n{player_list}  num = {player_num}")

game = True
while game:
    player_chek = input("contiune fo game 'hit' or finish this game 'stand':\n") .lower()
    if player_chek == "hit":
        random_player = random.choice(cards)
        player_list.append(random_player)
        player_num += player_list[-1]
        print(f"Your cards: \n{player_list}  num = {player_num}")
        if player_num > 21:
            print("lost !!")
            game = False
    elif player_chek == "stand":
        computer = True
        while computer:
            random_ia_chek = random.choice(chek_list)
            print(random_ia_chek)
            if random_ia_chek == "hit":
                random_ia = random.choice(cards)
                ia_list.append(random_ia)
                ia_num += ia_list[-1]
                print(f"Computer cards: \n{ia_list}  num = {ia_num}")
                if ia_num > 21:
                    print("win !!")
                    game = False
            elif random_ia_chek == "stand":
                if ia_num > player_num:
                    print(f"Lost Ia num = {ia_num}, Your num = {player_num}")
                    game = False
                elif ia_num == player_num:
                    print(f"Draw Ia num = {ia_num}, Your num = {player_num}")
                    game = False
                else:
                    print(f"Win Ia num = {ia_num}, Your num = {player_num}")
                    game = False
                computer = False
                game = False



            




