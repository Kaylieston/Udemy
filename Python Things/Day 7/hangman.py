
#TODO 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it. 
#TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO 3 - Check if the letter the user guessed is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not. 

import random
def hangman():
    
    print(""" 
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/ 
        """)


    words = [
        "apple", "banana", "cherry", "grape", "kiwi", "lemon", "orange", "peach", "pear", "plum",
        "dog", "cat", "elephant", "giraffe", "hippopotamus", "kangaroo", "lion", "monkey", "tiger", "zebra",
        "computer", "keyboard", "mouse", "monitor", "laptop", "tablet", "smartphone", "software", "hardware", "internet",
        "ocean", "mountain", "desert", "forest", "river", "lake", "waterfall", "volcano", "canyon", "island",
        "car", "bike", "bus", "train", "airplane", "boat", "truck", "bicycle", "motorcycle", "scooter",
        "book", "pen", "pencil", "paper", "notebook", "eraser", "sharpener", "ruler", "scissors", "glue",
        "holiday", "vacation", "trip", "adventure", "journey", "excursion", "exploration", "tour", "tourist", "destination"
    ]

    # Generate random word
    chosen_word = random.choice(words)
    # Create blanks follow the word length: 
    blanks = "_" * len(chosen_word)
    blanks_list = list(blanks)

    print(chosen_word)
    print(f"Word to guess: {blanks}")

   


    lives = 6
    while lives <= 6: 
         # Simulate user guessing letters
        user_guess = input("Guess a letter: ").lower()
        
        if user_guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == user_guess:
                    blanks_list[index] = user_guess
                    print("Correct! Current word:", "".join(blanks_list))
                    print(f"********************* {lives}/6 LIVES LEFT ***********************")
                elif blanks_list == chosen_word:
                    print("<<<< CONGRATULATIONS! YOU WON THE GAME! >>>> ")  
        else: 
            print (f"~ You guessed {user_guess}, that's not in the word. You lose a life. ~ ")
            lives -= 1
            print("Current word:", "".join(blanks_list))
            print(f"********************* {lives}/6 LIVES LEFT ***********************")
            if lives == 0: 
                print(f"<<<< IT WAS {chosen_word}! YOU LOSE >>>>")
                return
    if blanks_list == chosen_word:
               print("<<<< CONGRATULATIONS! YOU WON THE GAME! >>>> ")        
    # Handle duplicate user_guess
    
hangman()


# while "_" in blanks: # ==> May need to use For LOOP to limit the time to 6 times
#     # Ask for user guess input
#     user_guess = str(input("Guess a letter: ")).lower()
#     # Check if the guess letter is in the chosen word
#     if user_guess in chosen_word:
#         print("Right")
#     else: 
#         print("Wrong!")
        

        
