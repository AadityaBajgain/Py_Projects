import random

# range_of_number 
a,b = int(input("from: ")),int(input("to: "))

# ask user for their choice of the number between the given range
while True:
    user_choice = int(input("Choose the number betweent the given range for the computer to guess: "))
    if user_choice >= a and user_choice <= b:
        break
# list to hold the number choosed randomly by the computer
rand_choise_list=[]
while True:
    computer_guess = random.randint(a,b)
    print(computer_guess)
    # if number already exist in the list then number will not be appended in the list
    if computer_guess not in rand_choise_list:
        rand_choise_list.append(computer_guess)
    
        if rand_choise_list[len(rand_choise_list)-1] == user_choice:
            print("computer guessed right")
            break
        print("wrong choice computer!!")
    else:
        print("number already exist in the list")
print(rand_choise_list)
print("game over")