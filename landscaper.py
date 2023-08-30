game_data = {
    "money": 0,
    "scissors_counter": 0,
    "lawnmower_counter": 0,
    "battery_lawnmower_counter":0,
    "quit":False
}
while(True):
    user_input= int(input("""
                What would you like to do?
                [1] Using my teeth and earn $5
                [2] Buy a pair of rusty scissors for $5
                [3] Use my rusty scissors and earn $5
                [4] buy old-timey push lawnmower for $25
                [5] Use my old lawnmower and earn $50
                [6] Buy fancy battery-powered lawnmower for $250
                [7] Use  my battery-powered and earn $100
                [8] Quit the Game
                """))
    if (user_input == 1):
        game_data["money"]+=1
        print(f"You have ${game_data['money']} in your account")
########################################   
##Option 2
########################################
    if(user_input == 2):
        if(game_data["money"]>=5):
            if(game_data["scissors_counter"] < 1):
                game_data["money"]= game_data["money"]- 5
                game_data["scissors_counter"]= 1
                print(f"Now You have ${game_data['scissors_counter']}scissors")
                print(f"Congratulations, Now You have ${game_data['money']}in your account")
            else:
                print(f"Now You have one pair of rusty scissors.")
        else:
            print("You do not have enough money")
########################################   
##Option 3
########################################
    if(user_input == 3):
        if(game_data["scissors_counter"]==1):
          game_data["money"]+=5
          print(f"Congratulations,You have now ${game_data['money']} in your account before purchase.") 
        else:
          print("You do not have rusty scissors, select option[2] to buy the scissors ")
########################################   
##Option 4
########################################
    
    if(user_input == 4):
            if(game_data["money"]>=25):
                if(game_data["lawnmower_counter"] < 1):
                    game_data["money"]= game_data["money"]- 25
                    game_data["lawnmower_counter"]= 1
                    print(f"Now You have ${game_data['lawnmower_counter']}lawnmower")
                    print(f"Now You have ${game_data['money']}in your account")
                else:
                    print(f"Now You have one pair of lawnmower.")
            else:
                print("You do not have enough money")

########################################   
##Option 5
########################################

    if(user_input == 5):
        if(game_data["lawnmower_counter"]==1):
            game_data["money"]+= 50
            print(f"Congratulations,You have now ${game_data['money']} in your account before purchase.") 
        else:
            print("You do not have lawnmower, select option[3] to buy the lawnmower ")

########################################   
##Option 6
########################################
  
    if(user_input == 6):
            if(game_data["money"]>=250):
                if(game_data["battery_lawnmower_counter"] < 1):
                    game_data["money"]= game_data["money"]- 250
                    game_data["battery_lawnmower_counter"]= 1
                    print(f"Now You have ${game_data['battery_lawnmower_counter']}battery lawnmower")
                    print(f"Now You have ${game_data['money']}in your account")
                else:
                    print(f"Now You have one pair of battery lawnmower.")
            else:
                print("You do not have enough money")
########################################   
##Option 7
########################################
    
    if(user_input == 7):
        if(game_data["battery_lawnmower_counter"]==1):
            game_data["money"]+= 100
            print(f"Congratulations,You have now ${game_data['money']} in your account before purchase.") 
        else:
            print("You do not have lawnmower, select option[5] to buy the battery ")



########################################   
##Option 8
########################################
  
    if(user_input == 8):
            if(game_data["money"]>=250):
                if(game_data["battery_lawnmower_counter"] < 1):
                    game_data["money"]= game_data["money"]- 250
                    game_data["battery_lawnmower_counter"]= 1
                    print(f"Now You have ${game_data['battery_lawnmower_counter']}battery lawnmower")
                    print(f"Now You have ${game_data['money']}in your account")
                else:
                    print(f"Now You have one pair of battery lawnmower.")
            else:
                print("You do not have enough money")
    
            


    if(user_input == 7):
        game_data["quit"]= True

    if (game_data["quit"] == True):
        print("you quit the game")
        break
    if(game_data["money"]>=100):
        print("You win")
        break

