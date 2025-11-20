# #18-21 wrist band
#
#
#
# age = input("How old are you: ")
# if age:
#     age = int(age)
#     if age >= 18 and age <=21:
#         print("You can enter but you need a wrist band!")
#     elif age >= 21:
#         # 21+ drink, normal entry
#         print("you are good to enter and can drink!")
#     else:
#         # too young, sorry
#         print("You cannot come in, you are too young :(")
# else:
#     print("Please enter an age!")




c1 = "rock"
c2 = "paper"
c3 = "scissors"
print("welcome to a game of rock, paper, scissors")

p1 = input("Player one, what is your choice: ")
p2 = input("Player two, what is your choice: ")

if p1 == "rock" and p2 == "scissors":
    print("player one wins with")
elif p1 == "scissors" and p2 == "rock":
    print(f"player two wins with")
elif p1 == "paper" and p2 == "scissors":
    print("player two wins")
elif p1 == "scissors" and p2 == "paper":
    print("player one wins ")
elif p1 == "paper" and p2 == "rock":
    print("player one wins")
elif p1 == "rock" and p2 == "paper":
    print("player two wins")
elif p1 == "rock" and p2 == "rock" or p1 == "paper" and p2 == "paper" or p1 == "scissors" and p2 == "scissors":
    print("It is a draw, go again")
else:
    print("Please enter a choice.")
