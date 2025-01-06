# def greet(name):
#     print(f"Hello {name}")
#     print(f"How are you, {name}?")
#     print(f"How do you do {name}?")
    
# greet("Kaylie")

# def life_in_weeks(age):
#     weeks_remain = (90 - age) * 52
#     print(f"You have {weeks_remain} weeks left.")

# life_in_weeks(20)

def calculate_love_Score(name1, name2):
    true = "TRUE".lower()
    love = "LOVE".lower()
    name1 = name1.lower()
    name2 = name2.lower()
    
    print("TRUE MATCH")
    # Count true match name 1:
    count_name1_true = 0
    for count1 in name1:
        for letter in true:
            if count1 == letter:
                count_name1_true += 1
    print(f"Name1 matches is: {count_name1_true}")
    # Count true match name 2:
    count_name2_true = 0
    for count2 in name2:
        for letter in true:
            if count2 == letter:
                count_name2_true += 1 
    print(f"Name2 matches is: {count_name2_true}")
    # Count total TRUE match 
    match_true = count_name1_true + count_name2_true
    print(f"The number of TRUE matches is: {match_true}")
    
    print("LOVE MATCH")
    # Count LOVE match name 1:
    count_name1_love = 0 
    for count1 in name1:
        for letter in love:
            if count1 == letter:
                count_name1_love += 1
    print(f"Name1 matches is: {count_name1_love}")
    # Count LOVE match name 2:
    count_name2_love = 0
    for count2 in name2:
        for letter in love:
            if count2 == letter:
                count_name2_love += 1
    print(f"Name2 matches is: {count_name2_love}")
    # Count total LOVE match:
    match_love = count_name1_love + count_name2_love
    print(f"The number of LOVE match is: {match_love}")
    
    # Total love Score
    love_score = str(match_true) + str(match_love)
    print(f"==> THE FINAL LOVE SCORE IS: {love_score}")
 
calculate_love_Score("HikariMoon", "Nukuruma Natsuki") 
       