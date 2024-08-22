import random

# for selection of random alphabets and symbols for the password
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
symbols='!@#$%^&*()_+'
numbers='1234567890'



def random_password():

    # user's choice word or phrase
    user_phrase = str(input("Enter the word or the phrase you want to include in your password: "))
    # list that carries all element of the password
    random_list=[]
    # for generating random alphabets and so on
    random_uppercase = random.choice(uppercase)
    random_lowercase = random.choice(lowercase)
    random_symbol= random.choice(symbols)
    random_number = random.choice(numbers)
    random_list.append(random_lowercase)
    random_list.append(random_uppercase)
    random_list.append(random_number)
    random_list.append(random_symbol)

    for i in user_phrase:
        random_list.append(i)

    random.shuffle(random_list)
    random_password_generated=''.join(i for i in random_list)
   
    print(f"Your random password generated is {random_password_generated}.")

random_password()

