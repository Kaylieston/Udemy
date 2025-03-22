student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 90:
        student_grades[student] = "Outstanding"
    elif score >= 80: 
        student_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else: 
        student_grades[student] = "Fail"
        
print(student_grades)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# # Nested List in Dictionary 
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# # Print Lille
# print(travel_log["France"][1])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# List in a List 
nested_list = ["A","B", ["C", "D"]]

# Print D 
print(nested_list[2][1])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Dictionary in a Dictionary

travel_log ={
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }, 
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
