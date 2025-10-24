import random
player = int(input("Choose a number from 1 to 3 :"))


if player not in [1, 2, 3]:
    print("Invalid input. Please choose a number from 1 to 3.")
    player = int(input("Choose a number from 1 to 3 :"))
    
elif player == 1:
    print("✊")
elif player == 2:
    print("✋")
elif player == 3:
    print("✌")
 
computer = random.randint(1,3)

if computer == 1:
    print("✊")
elif computer == 2:
    print("✋")     
elif computer == 3:
    print("✌")


if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2 :
        
    print("Player wins!")
elif player == computer:
    print("It's a tie!")
else:
    print("Computer wins!")

        
        


