alphabet = ['a','b','c','d','e','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]


def ceassar(original_text, shit_amount, encode_or_decode):

    output_text = ""
    if encode_or_decode == "decode":
        shit_amount *= -1
    elif encode_or_decode == "encode":
         shit_amount *= 1
    else:
        print("Please enter a correct value (decode or encode)")
        
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            cipher_word = alphabet.index(letter) + shit_amount
            cipher_word %= len(alphabet)
            output_text += alphabet[cipher_word]
    print(f"decoded: {output_text}")

continue_program = True 

while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    if direction == "encode" or  direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    

        ceassar(text, shift, direction)

        chek = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

        if chek == "no":
            continue_program = False
            print("by by by")
