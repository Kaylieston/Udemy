""" TIP CALCULATOR """

# Introduction 
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
customer_tip = int(input("How much tip you would like to give? 10%, 12%, or 15%? "))
people_number = int(input("How many people to split the bill? "))

# Not forcing the user to input the specified tips amount 
per_person_amount = round((total_bill + (total_bill * customer_tip / 100)) / people_number, 2)

print(f"Each person should pay: ${per_person_amount}")

