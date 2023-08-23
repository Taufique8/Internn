import random
def fiza():
    user = input("Enter a choice ( Rock,Paper,Scissors): ")
    option = [ "rock","paper","scissors"]
    ai = random.choice(option)
    choices = {"Player": user,"computer": ai}
    return choices
def check(player,computer):
    print("you chose", player, "computer chose", computer)
    if player==computer:
        return "it`s a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win"
        else:
            return "Paper cover rock! you lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper cover rock! You Win"
        else:
            return "scissors cut paper, you lose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper! You Win"
        else:
            return "Rock smashes scissors! you lose"
choices = fiza()
result = check(choices["Player"],choices["computer"])
print(result)
            


    

