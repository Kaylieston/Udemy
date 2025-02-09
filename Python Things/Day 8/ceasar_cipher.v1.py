alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Keep asking until the user enters "encode" or "decode"
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").strip().lower()
    
    if direction in ["encode", "decode"]:
        break # Exit the loop if input is invalid 
    else: 
        print("INAVLID INPUT.\n ========================")

    # Collecting the rest input         
    original_text = input("Type your message:\n").lower()#
    shift_amount = int(input("Type the shift number:\n"))

def cipher():
    
    # TODO-1: Create a function called encrypt() that makes original_text and shift_amount as 2 inputs
    # TODO-2: Inside the "encrypt" fucntion, shift each letter of the original_text forwards in the alphabet by the shift_Amount and print the encrypted text. 
    # TODO-3: Call the'encrypt()' fucntion and pass in the user inputs. You should be able to test the code and encrypt a message  
    # TODO-4: what happens if you try to shift z forwards by 9? Can you fix the code?


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

            
    def decrypt (original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) - shift_amount
                cipher_text += alphabet[shifted_position]
            else: 
                cipher_text += letter 
            
        return f"Here is the decoded result: {cipher_text}"

    # Call the correct function
    if direction == "encode":
        print(encrypt(original_text, shift_amount))
    elif direction == "decode": 
        print(decrypt(original_text, shift_amount))
    
    # Return the function 
    return cipher() 
    

next_action = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")

if next_action in ["yes", "no"]:
    if next_action == "yes":
        print(cipher())
    elif next_action == "no":
        print("Thank you for using our service. Goodbye!") 
        
else:
    print("INVALID INPUT.\n ========================")


    