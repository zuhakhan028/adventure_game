user_name=input("type your name here: ").lower()
print("Welcome to the adventure game {}".format(user_name))

user_choice=input("which path would you dare to choose (left/right)?  ").lower()

if user_choice=="left":
    user_choice=input("would you like to swim accorss the river or just take a walk along side ? (swim/walk) ").lower()
    if user_choice=="swim":
        print("opps! an alligator ate you! YOU LOST")
    elif user_choice=="walk":
        print("seems like a coconut just dropped on your head! your eliminated.")
    else:
        print("you choose a wrong option! you lost!")

elif user_choice=="right":
    user_choice=input("you came across a broken bridge.would you like to move ahead or go back? (ahead/ back)? ").lower()
    if user_choice=="ahead":
        user_choice=input("uhmm you bumped into a stranger would you like to talk to him? (yes/no)").lower()
        if user_choice=="yes":
            print("starnger gifted you so much food! enjoy your meal")
            print("YOU WON!")
        elif user_choice=="no":
            print("you are an introvert ! you missed a meal, you lost!")
        else:
            print("you choose a wrong option! you lost!")
else:
    print("you choose a wrong option! you lost!")

print("THANK YOU FOR TRYING {}".format(user_name))

