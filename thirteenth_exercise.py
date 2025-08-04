import random
num = random.randint(1, 20)
guess_count = 0
guess_num = 0
while guess_count < 3:
    guess_num = int(input("Guess a number between 1 and 20: "))
    if guess_num > 20:
        print("Too high number please enter a number lower than 20")
        continue
    if guess_num == num:
        print("Congratulations! You guessed the number correctly!")
        break
    else:
        print("Sorry, that's wrong.")
    guess_count += 1
if guess_count == 3:
    print("You lose the game")