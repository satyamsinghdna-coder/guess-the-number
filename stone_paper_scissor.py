import random

def game1():
    comput_choice = ("Paper", "Stone", "Scissor")

    win = 0
    lose = 0

    while True:
        computer_choice = random.choice(comput_choice)

        print("\n" + "🟦" * 40)
        print("🎮 Welcome to The Rock Paper Scissor Game 🎮")
        print("🟦" * 40)

        user_choice = input("🎯 Enter Your Turn: ")

        if computer_choice == "Stone":

            if user_choice in ("Stone", "stone", "S", "s", "Rock", "rock", "r", "R"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 🥌 Stone")
                print("👤 Your Choice: 🥌 Stone")
                print("🤝 Draw!")
                print("🟩🟨" * 20)

            elif user_choice in ("Paper", "paper", "P", "p"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 🥌 Stone")
                print("👤 Your Choice: 📃 Paper")
                print("🏆 Winner!")
                win += 1
                print("🟩🟨" * 20)

            elif user_choice in ("Scissor", "scissor", "Sc", "sc"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 🥌 Stone")
                print("👤 Your Choice: ✂️ Scissor")
                print("💔 Loser!")
                lose += 1
                print("🟩🟨" * 20)

            else:
                print("⚠️ Please Enter a Valid Spelling")


        if computer_choice == "Paper":

            if user_choice in ("Stone", "stone", "S", "s", "Rock", "rock", "r", "R"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 📃 Paper")
                print("👤 Your Choice: 🥌 Stone")
                print("💔 Loser!")
                lose += 1
                print("🟩🟨" * 20)

            elif user_choice in ("Paper", "paper", "P", "p"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 📃 Paper")
                print("👤 Your Choice: 📃 Paper")
                print("🤝 Draw!")
                print("🟩🟨" * 20)

            elif user_choice in ("Scissor", "scissor", "Sc", "sc"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: 📃 Paper")
                print("👤 Your Choice: ✂️ Scissor")
                print("🏆 Winner!")
                win += 1
                print("🟩🟨" * 20)

            else:
                print("⚠️ Please Enter a Valid Spelling")


        if computer_choice == "Scissor":

            if user_choice in ("Stone", "stone", "S", "s", "Rock", "rock", "r", "R"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: ✂️ Scissor")
                print("👤 Your Choice: 🥌 Stone")
                print("🏆 Winner!")
                win += 1
                print("🟩🟨" * 20)

            elif user_choice in ("Paper", "paper", "P", "p"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: ✂️ Scissor")
                print("👤 Your Choice: 📃 Paper")
                print("💔 Loser!")
                lose += 1
                print("🟩🟨" * 20)

            elif user_choice in ("Scissor", "scissor", "Sc", "sc"):
                print("\n" + "🟩🟨" * 20)
                print("🤖 Computer: ✂️ Scissor")
                print("👤 Your Choice: ✂️ Scissor")
                print("🤝 Draw!")
                print("🟩🟨" * 20)

            else:
                print("⚠️ Please Enter a Valid Spelling")


        print("\n" + "➖" * 40)
        print("🏆 Your Score: ", win)
        print("🤖 Computer Score: ", lose)
        print("➖" * 40 + "\n")