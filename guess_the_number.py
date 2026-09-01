import random
def show_rules():
    print("\n","="*80,"\nGuess The Number Between 1 and 100")
    print("You Have only 7 attempts")
play = 0
score=0
while True:
    num = random.randint(1,100)
    attempts=0
    while attempts<=6:
        show_rules()
        try:
            guess = int(input("Enter Your Guess: "))
            if guess>num:
                print("Your Guess is too High⏫")
                attempts+=1
            elif guess<num:
                print("Your Guess is too Low⏬")
                attempts+=1
            else:
                attempts+=1
                print("Your Guess is Correct✅\n You Guess The Number in",attempts,"Attempts")
                play = 1
                score +=1
                break
        except ValueError:
            print("Please Enter Only Numbers")
            continue
    if play ==1:
        print("You Are Winner")
        print("Score: ",score)
        play=0
    else:
        print("Game over")
        print("Score: ",score)
    
    print("-"*80,"\nChoices","-"*80)
    print("1.Play Again")
    print("2.Exit")
    try:
        a = int(input("Enter Your Choice"))
        if a == 1:
            continue
        if a == 2:
            break
        else:
            print("Please Enter Only Numbers 1 or 2")
    except ValueError:
        print("Please Enter Only Numbers 1 or 2")
        
            