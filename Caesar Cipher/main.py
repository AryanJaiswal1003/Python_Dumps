from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, user_preference):
    output_text = ""

    # Adjust shift direction once based on user preference
    if user_preference == "decode":
        shift_amount *= -1 # Only difference b/w Encode & Decode function is (+ve / -ve) value of shift amount.

    for letter in original_text:
        
        if letter not in alphabet:  # Figuring: What happens if the user enters a number/symbol/space
            output_text += letter
        
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {user_preference}d result: {output_text}")

game_over = True # Way to Restart the cipher program

while game_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, user_preference=direction)

    restart = input("Type 'Yes' if you want to Continue or else Type 'No':\n").lower()
    if restart == 'no':
        game_over = False
        print("################ Thankyou For Choosing our Services!! ################")