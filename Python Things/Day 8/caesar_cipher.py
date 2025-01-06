alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
original_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

# TODO-1: Create a function called encrypt() that makes original_text and shift_amount as 2 inputs
# TODO-2: Inside the "encrypt" fucntion, shift each letter of the original_text forwards in the alphabet by the shift_Amount and print the encrypted text. 
# TODO-4: what happens if you try to shift z forwards by 9? Can you fix the code?
# TODO-3: Call the'encrypt()' fucntion and pass in the user inputs. You should be able to test the code and encrypt a message  


x = alphabet.index("c")

def encrypt(original_text, shift_amount):
    for letter in original_text:
        for character in alphabet: 
            if letter == character: 
                shift_text = alphabet.index(shift_amount)
    print(shift_text)