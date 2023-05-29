import random

users_choice=input("Enter your move(Rock,Paper,Scissor):")
computers_choice= random.choice(["Rock","Scissor","Paper"])

print(users_choice,computers_choice)

if users_choice==computers_choice:
    print("Match tied")

elif users_choice =="Rock":
    if computers_choice == "Paper":
        print("paper covers Rock, Computer wins")
    else:
        print("Rock smashes Scissor, You won")
elif users_choice =="Paper":
    if computers_choice == "Scissor":
        print("Scissor cuts Paper, Computer wins")
    else:
        print("Paper covers Rock, You won")
elif users_choice =="Scissor":
    if computers_choice == "Rock":
        print("Rock smashes Scissor, Computer wins")
    else:
        print("Scissor cuts paper, You won")        