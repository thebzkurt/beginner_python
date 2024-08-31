import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
chek_list = ["hit","stand"]
ia_list = []
ia_list_secret = ["*"]
player_list = []

player_num = 0
ia_num = 0
random_ia = 0
random_player = 0

#fonksiyonlar 
def adding(user,list = list):
    user = random.choice(cards)
    list.append(user)

def numdef(num_list):
    total = 0
    for numbers in num_list:
        total += numbers
    return total

def game_chek(computer, player):
    if computer > player:
        print(f"******** Player Lost ********\nIa num = {computer}, Your num = {player}")
        game = False
    elif computer == player:
        print(f"******** Draw ********\nIa num = {computer}, Your num = {player}")
        game = False
    else:
        print(f"******** Player Win ********\nIa num = {computer}, Your num = {player}")
        game = False


    pass

#baslangic icin alinan 2 random sayi
beginning = True
while beginning:

    adding(random_ia, ia_list)
    adding(random_player,player_list)

    if 2 == len(ia_list) and 2 == len(player_list):
        beginning = False

#alinan random sayilari toplayan alan ve bunlarin ciktida gozlenmesini saglayan diger kodlar
player_num = numdef(player_list)
ia_num = numdef(ia_list)
ia_list_secret.append(ia_list[1])

print(f"Computer cards: \n{ia_list_secret}  num = {ia_num - ia_list[0]}")
print(f"Your cards: \n{player_list}  num = {player_num}")

game = True
while game:
    #kulanicinin yaptigi secimleri sorgulayan dongu
    player_chek = input("\ncontiune fo game 'hit' or finish this game 'stand':\n") .lower()
    if player_chek == "hit":
        adding(random_player,player_list)
        player_num += player_list[-1]
        print(f"Your cards: \n{player_list}  num = {player_num}")
        if player_num > 21:
            print("\n************************* Player Lost *************************")
            game = False
    elif player_chek == "stand":
        computer = True
        # bilgisayarin secimler yatigi kisimlar
        while computer:
            random_ia_chek = random.choice(chek_list)
            print(f"\ncomputer choice = {random_ia_chek}\n***************")
            if random_ia_chek == "hit":
                adding(random_ia, ia_list)
                ia_num += ia_list[-1]
                ia_list_secret.append(random_ia)
                if ia_num > 21:
                    print("\n************************* Player Win *************************")
                    print(f"Computer cards: \n{ia_list}  num = {ia_num}\n")
                    print(f"Your cards: \n{player_list}  num = {player_num}\n")
                    computer = False
                    game = False
                else:
                    print(f"Computer cards: \n{ia_list_secret}  num = {ia_num - ia_list[0]}")
            elif random_ia_chek == "stand":
                print(f"Computer cards: \n{ia_list}  num = {ia_num}")
                print("*********************************************")
                print(f"Your cards: \n{player_list}  num = {player_num}")
                game_chek(ia_num,player_num)
                computer = False
                game = False



            




