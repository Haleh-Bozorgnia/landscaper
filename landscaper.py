game_data = {
    "money": 0,
    "scissors_counter": 0,
    "lawnmower_counter":0,
    "battery_lawnmower_counter":0,
    "quit":False
}
while(True):
    user_input= int(input("""
                What would you like to do?
                [1] Using my teeth
                [2] Buy a pair of rusty scissors for $5
                [3] Use my rusty scissors
                [4] buy old-timey push lawnmower for $25
                [5] fancy battery-powered lawnmower for $250
                [6] Use  my battery-powered
                [7] Quit the Game
                """))
    if (user_input == 1):
        game_data["money"]+=1
        print(f"You have ${game_data['money']} in your account")
       
    if(user_input == 2):
        if(game_data["money"]>=5 and game_data["scissors_counter"]<1 ):
            print(f"You have now ${game_data['money']} in your account before purchase.")
            game_data["money"]= game_data["money"] -5 
            game_data["scissors_counter"]+=1
            print(f"You have now ${game_data['money']} in your account after purchase.")
        elif(game_data["scissors_counter"]==1):
            print("You cab buy pair of rusty scissors one time")
        else:
            print("You do not have enought money to buy pair of rusty scissors.")

    if(user_input == 3):
        if(game_data["scissors_counter"]==1):
          game_data["money"]+=5
          print(f"You have now ${game_data['money']} in your account before purchase.") 
        else:
            print("You do not have rusty scissors, select option[2] to buy the scissors ")

    if(user_input == 4):
        if(game_data["money"]>=25 and game_data["lawnmower_counter"]==0 and game_data["scissors_counter"]==1):
            print(f"You have now ${game_data['money']} in your account before purchase.")
            game_data["money"]= game_data["money"] -25 
            game_data["lawnmower_counter"]+=1
            print(f"You have now ${game_data['money']} in your account after purchase.")
        elif(game_data["scissors_counter"]==0 and game_data["money"]>=25):
            print("You do not have scissors")
        elif(game_data["lawnmower_counter"]==1 and game_data["money"]>=25 and game_data["scissors_counter"]==1):
            print("You can buy lawnmower one time")
        else:
            print("You do not have enought money to buy pair of rusty scissors.")

    if(user_input == 5):
        if(game_data["money"]>=26): 
            if( game_data["lawnmower_counter"]==1):
                if(game_data["battery_lawnmower_counter"]==0):
                   print(f"You have now ${game_data['money']} in your account before purchase.")
                   game_data["money"]= game_data["money"] -26 
                   game_data["battery_lawnmower_counter"]+=1
                else:
                    print("You have one battery lawnmower")
            else:
                print("You do not have any lawnmower")
        else:
            print("You do not have enought money to buy battery lawnmower.")

    if(user_input == 6):
        if(game_data["battery_lawnmower_counter"]==1):
             game_data["money"]= game_data["money"]+ 100
             print(f"You have now ${game_data['money']} in your account before purchase.")


    
            


    if(user_input == 7):
        game_data["quit"]= True

    if (game_data["quit"] == True):
        print("you quit the game")
        break
    if(game_data["money"]>=100):
        print("You win")
        break

