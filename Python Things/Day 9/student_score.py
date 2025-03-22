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

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary 
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["France",])