#Created 9/30/2021
#By Wolfetone

ALPHABET = {"a":".-","b":"-...","c":"-.-.",
            "d":"-..","e":".","f":"..-.",
            "g":"--.","h":"....","i":"..",
            "j":".---","k":"-.-","l":".-..",
            "m":"--","n":"-.","o":"---",
            "p":".--.","q":"--.-","r":".-.",
            "s":"...","t":"-","u":"..-",
            "v":"...-","w":".--","x":"-..-", 
            "y":"-.--","z":"--.."}

def encrypt(message):
    encrypted_cipher = ""
    for letter in message:
        if letter != " ":
            encrypted_cipher += ALPHABET[letter] + " "
    return encrypted_cipher

print(encrypt("hello"))


