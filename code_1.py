import random

user_score = 0
bot_score = 0

while user_score < 2 and bot_score < 2:
    print("---------------------------------------")
    inp = input("Enter Rock, Paper, or Scissor: ")

    if inp.lower() not in ["rock", "paper", "scissor"]:
        print("Invalid input. Please enter Rock, Paper, or Scissor.")
        continue

    Bot = random.choice(["rock", "paper", "scissor"])

    print("You -", inp)
    print("Bot -", Bot)

    if (inp.lower() == "rock" and Bot == "scissor") or (inp.lower() == "paper" and Bot == "rock") or (inp.lower() == "scissor" and Bot == "paper"):
        print("You won")
        user_score += 1
    elif (inp.lower() == "rock" and Bot == "paper") or (inp.lower() == "paper" and Bot == "scissor") or (inp.lower() == "scissor" and Bot == "rock"):
        print("Bot won")
        bot_score += 1
    elif (inp.lower() == "rock" and Bot == "rock") or (inp.lower() == "paper" and Bot == "paper") or (inp.lower() == "scissor" and Bot == "scissor"):
        print("It's a tie")
    else:
        print("Invalid input")

print("---------------------------------------")
if user_score > bot_score:
    print("You won the best of three!")
elif user_score < bot_score:
    print("Bot won the best of three!")
else:
    print("It's a tie in the best of three!")
