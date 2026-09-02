import guess_the_number
import stone_paper_scissor

print("=" * 50)
print("What Do You Want To Play?")
print("1. Guess The Number")
print("2. Rock Paper Scissors")

choice = input("Enter Your Choice: ")

if choice == "1":
    guess_the_number.game2()
elif choice == "2":
    stone_paper_scissor.game1()


else:
    print("Please Enter Only Numbers 1 or 2")