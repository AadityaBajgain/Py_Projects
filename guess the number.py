import random
a=int(input("From: "))
b=int(input("To: "))
rand_num = random.randint(a,b)

# print(rand_num)

while True:
    user_guess = int(input("Guess the number between a and b: "))
    if user_guess == rand_num:
        print("you guessed the correct number!! you won")
        break
    print("no you are wrong")

print("you compleated the game")