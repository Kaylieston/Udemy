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
        print(f"Here is the decoded result: {output_text}") 
        
    elif direction =="encode":
        print(encrypt(original_text, shift_amount))
    else: 
        print("INVALID INPUT.\n========================")
            
cipher(original_text, shift_amount, direction)

next_action = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

if next_action in ["yes", "no"]:
    if next_action == "yes":
        encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()      
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print(cipher(original_text=text, shift_amount=shift, direction=encode_or_decode))
    elif next_action == "no":
        print("Thank you for using our service. Goodbye!") 

else:
    print("INVALID INPUT.\n ========================")  
