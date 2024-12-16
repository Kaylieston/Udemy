# student_score = [150, 142, 185, 149, 24, 60, 68, 199, 78, 65, 89, 76, 86, 12]

# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score
# print(max_score)


# # Write code to automatically sum from 1 to 100, inclusive of both 1 and 100
# total = 0

# for number in range(1, 101):
#     total += number
# print(total)

# """
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# """
# for number in range(1, 101): 
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0: 
#         print("Buzz")
#     else: 
#         print(number)
   
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""KAYLIE'S ANSWER"""
#Password Generator Project
def random_generated_pass ():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_numbers = int(input("How many numbers would you like?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # If returns UNIQUE characters 
    if nr_letters > len(letters) or nr_numbers > len(numbers) or nr_symbols > len(symbols):
        print("Error: You requested more characters than available in one or more categories")
        return
    else: 
        random_letters = random.sample(letters, nr_letters)
        random_numbers = random.sample(numbers, nr_numbers)
        random_symbols = random.sample(symbols, nr_symbols)

    random_password = random_letters + random_numbers + random_symbols

    # Final password --> No need to use Loop
    for random_final_pass in random_password:
        final_result = "".join(random_final_pass)
        print("==> Your ultimate secured password is: " + final_result)

    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    random_order_password = random.shuffle(random_password)

    for random_order_password in random_password:
        final_random_order_result = "".join(random_order_password)
        print("==> Another option for you: " + final_random_order_result)

    
random_generated_pass()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""VUONG BOOF'S ANSWER"""
def random_generated_pass ():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_numbers = int(input("How many numbers would you like?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # If returns UNIQUE characters 
    if nr_letters > len(letters) or nr_numbers > len(numbers) or nr_symbols > len(symbols):
        print("Error: You requested more characters than available in one or more categories")
        return
    else: 
        random_password =   random.sample(letters, nr_letters) + \
                            random.sample(numbers, nr_numbers) + \
                            random.sample(symbols, nr_symbols)

    # Final password 
    print("==> Your ultimate secured password is: " + "".join(random_password))

    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    random_order_password = random.shuffle(random_password)

    print("==> Another option for you: " + "".join(random_password))
    
    
random_generated_pass()
