game_data = {
    "money": 0,
    "buy_scissors_counter": 0,
    "quit":False
}
while(True):
    user_input= int(input("""
                What would you like to do?
                [1] Using my teeth
                [2] Buy a pair of rusty scissors for $5
                [3] Quit the Game
                """))
    if (user_input == 1):
        game_data["money"]+=1
        print(f"You have ${game_data['money']} in your account")
       
    if(user_input == 2):
        if(game_data["money"]>=5 and game_data["buy_scissors_counter"]<1 ):
            print(f"You have now ${game_data['money']} in your account before purchase.")
            game_data["money"]= game_data["money"] -5 
            game_data["buy_scissors_counter"]+=1
            print(f"You have now ${game_data['money']} in your account after purchase.")
        elif(game_data["buy_scissors_counter"]==1):
            print("You cab buy pair of rusty scissors one time")
        else:
            print("You do not have enought money to buy pair of rusty scissors.")


    if(user_input == 3):
        game_data["quit"]= True

    if (game_data["quit"] == True):
        print("you quit the game")
        break
    if(game_data["money"]>=100):
        print("You win")
        break

