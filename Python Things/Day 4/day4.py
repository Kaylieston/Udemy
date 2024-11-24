# import my_module

# print(my_module.my_favorite_number)

# import random 
# random_string = random.choice(["Heads", "Tails"])
# print(random_string)

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# # 1 Option
# print(random.choice(friends))
#
# # 2 Option
# random_index = random.randint(0, 4)
# print(friends[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0]) # Print out the 1st list "fruits"
print(dirty_dozen[1]) # Print out the 2nd list "vegetables"

print(dirty_dozen[1][2]) # Print out the num.02 word in the 2nd list
print(dirty_dozen[1][3]) # Print out the num.03 word in the 2nd list

print(dirty_dozen[1][1]) # Print out the num.01 word in the 2nd list 
print(dirty_dozen[0][0]) # Print out the num.00 word in the 1st list 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

'''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

'''_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''