alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# # Keep asking until the user enters "encode" or "decode"
# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()

#     if direction in ["encode", "decode"]:
#         break # Exit the loop if input is invalid 
#     else: 
#         print("INAVLID INPUT.\n ========================")

#     # Collecting the rest input         
#     original_text = input("Type your message:\n").lower()#
#     shift_amount = int(input("Type the shift number:\n"))

# def cipher():

#     def encrypt(original_text, shift_amount):
#         cipher_text = "" 
#         for letter in original_text:
#             if letter in alphabet: # Ensure it's a valid letter 
#                 shifted_position = alphabet.index(letter) + shift_amount 

#                 shifted_position = shifted_position % len(alphabet) # To fix the code when user try to shift z forward
#                 cipher_text += alphabet[shifted_position]
#             else: 
#                 cipher_text += letter # Keep non-alphabet letter unchanged 

#         return f"Here is the encoded result: {cipher_text}" 
#     # Use return instead of print to ensure that the function is return 


#     def decrypt (original_text, shift_amount):
#         output_text = ""
#         for letter in original_text:
#             if letter in alphabet:
#                 shifted_position = alphabet.index(letter) - shift_amount
#                 cipher_text += alphabet[shifted_position]
#             else: 
#                 output_text_text += letter 

#         return f"Here is the decoded result: {output_text}"

#     # Call the correct function
#     if direction == "encode":
#         print(encrypt(original_text, shift_amount))
#     elif direction == "decode": 
#         print(decrypt(original_text, shift_amount))

#     # Return the function 
#     return cipher() 


# next_action = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

# if next_action in ["yes", "no"]:
#     if next_action == "yes":
#         print(cipher())
#     elif next_action == "no":
#         print("Thank you for using our service. Goodbye!") 

# else:
#     print("INVALID INPUT.\n ========================")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Another way to solve the problem without using the While loop

print("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88             
      
      """)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()      
original_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
        cipher_text = "" 
        for letter in original_text:
            if letter in alphabet: # Ensure it's a valid letter 
                shifted_position = alphabet.index(letter) + shift_amount 
            
                shifted_position = shifted_position % len(alphabet) # To fix the code when user try to shift z forward
                cipher_text += alphabet[shifted_position]
            else: 
                cipher_text += letter # Keep non-alphabet letter unchanged 
        
        return f"Here is the encoded result: {cipher_text}" 
    # Use return instead of print to ensure that the function is return 


def cipher(original_text, shift_amount, direction):
    
    output_text = ""
    
    if direction == "decode":
        shift_amount *= -1   
        for letter in original_text: 
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else: 
                output_text += letter
        return(f"Here is the decoded result: {output_text}") # Shoud use return instead of print since cipher() does not return any value 
        
    elif direction =="encode":
        print(encrypt(original_text, shift_amount))
    else: 
        print("INVALID INPUT.\n========================")
            
cipher(original_text, shift_amount, direction)

# Check if the user wants to go again - SOLUTION 1
should_continue = True

while should_continue:
    restart = input("========================\nType 'yes' if you want to go again. Otherwise type 'no'\n")
    if restart == "no":
        should_continue = False
        print("Thank you for using our service. Goodbye!") 
    elif restart == "yes":  
        encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()      
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    
        result = cipher(original_text=text, shift_amount=shift, direction=encode_or_decode) # Modify cipher() to result instead of printing inside the function, we should update the function call 
        print(result)
    else:
        print("INVALID INPUT.\n ========================")
        

# # Check if the user wants to go again - SOLUTION 22 - Could not repeat the cipher continously
# next_action = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

# if next_action in ["yes", "no"]:
#     if next_action == "yes":
#         encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()      
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
        
#         result = cipher(original_text=text, shift_amount=shift, direction=encode_or_decode) # Modify cipher() to result instead of printing inside the function, we should update the function call 
#         print(result)
#     elif next_action == "no":
#         print("Thank you for using our service. Goodbye!") 

# else:
#     print("INVALID INPUT.\n ========================")  


        

    
    
    