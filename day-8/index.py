# caesar cypher
import numbers
alphabet = "abcdefghijklmnopqrstuvwxyz"
# abcdefghijklmnopqrstuvwxyz
# jklmnopqrstuvwxyzabcdefghi
# qnuux fxaum
# 9
def caesar_cypher(shift):
    first_part, second_part = alphabet[:shift], alphabet[shift:]
    caesar_alphabet = second_part + first_part
    return caesar_alphabet

def caesar_cypher_encoder(text, shift):
    caesar_alphabet = caesar_cypher(shift)
    print(caesar_alphabet)
    cypher = ""

    positions = []
    for letter in text:
        if letter in alphabet:
            positions.append(alphabet.index(letter))
        else:
            positions.append(letter)
    
    for pos in positions:
        if isinstance(pos, numbers.Number) and not isinstance(pos, bool):
            cypher = cypher + caesar_alphabet[pos]
        else:
            cypher = cypher + pos
    return cypher

def caesar_cypher_decoder(text, shift):
    decoded_str = ""
    positions = []
    for letter in text:
        if letter in alphabet:
            positions.append(alphabet.index(letter) - shift)
        else:
            positions.append(letter)
    
    for pos in positions:
        if isinstance(pos, numbers.Number) and not isinstance(pos, bool):
            decoded_str = decoded_str + alphabet[pos]
        else:
            decoded_str = decoded_str + pos
    return decoded_str



# print(caesar_cypher_encoder("hello world", 9))
# print(caesar_cypher_decoder("qnuux fxaum", 9))

def caesar_game(): 
    print("Welcome to the Caesar Cypher Encoder/Decoder Game!")
    operation = input("Would you like to encode or decode a message? ")
    text = input("Please enter the message: ")
    shift = int(input("Please enter the shift value (0-25): "))

    if operation.lower() == "encode":
        encoded_message = caesar_cypher_encoder(text, shift)
        print(f"Encoded Message: {encoded_message}")
    elif operation.lower() == "decode":
        decoded_message = caesar_cypher_decoder(text, shift)
        print(f"Decoded Message: {decoded_message}")
    else:
        print("Invalid operation. Please choose 'encode' or 'decode'.")

caesar_game()