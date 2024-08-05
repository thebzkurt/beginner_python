import random 

global player_choes
global ui_chose
global player_score
global ui_score


player_score = 0
ui_score = 0
Game = ['paper','scissors','rock']

def GameTime():
    global player_choes
    global ui_chose
    for i in Game:
        print(i)
    player_choes = input(f"Please choose one : ")
    if player_choes in Game:
        print("****************************************\n")
    else:
        print("wrong!")
        return GameTime()

    ui_chose = random.choice(Game)
    print(f"player chose = {player_choes}")
    print("****************************************\n")
    print(f"ui chose = {ui_chose}")
    print("****************************************\n")
    

def GameControl():
        global player_choes
        global ui_chose
        global player_score
        global ui_score
        while player_score < 3 and ui_score < 3:
            GameTime()
            if player_choes == "paper" and ui_chose == "rock":
                print("Win")                 
                player_score += 1
            elif player_choes == "scissors" and ui_chose == "paper":
                print("win")
                player_score += 1
            elif player_choes == "rock" and ui_chose == "scissors":
                print("win")
                player_score += 1
            else:
                print("Lose")
                ui_score += 1
            
            print(f"Player Score: {player_score} - UI Score: {ui_score}")
            print("******************************************************\n")

        if int(player_score) > int(ui_score):
            print(f"Winner PLAYER **** ")
        else:
            print(f"Winner UI **** ") 

GameControl()          
                

            
        







        

    


