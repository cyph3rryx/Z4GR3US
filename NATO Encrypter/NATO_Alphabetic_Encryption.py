def nato_encrypt(message):
    nato_alphabet = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    encrypted_message = ""
    for letter in message:
        if letter.upper() in nato_alphabet:
            encrypted_message += nato_alphabet[letter.upper()] + " "
        else:
            encrypted_message += letter
    return encrypted_message.strip()

def nato_decrypt(message):
    nato_alphabet = {
        'Alfa': 'A', 'Bravo': 'B', 'Charlie': 'C', 'Delta': 'D',
        'Echo': 'E', 'Foxtrot': 'F', 'Golf': 'G', 'Hotel': 'H',
        'India': 'I', 'Juliet': 'J', 'Kilo': 'K', 'Lima': 'L',
        'Mike': 'M', 'November': 'N', 'Oscar': 'O', 'Papa': 'P',
        'Quebec': 'Q', 'Romeo': 'R', 'Sierra': 'S', 'Tango': 'T',
        'Uniform': 'U', 'Victor': 'V', 'Whiskey': 'W', 'Xray': 'X',
        'Yankee': 'Y', 'Zulu': 'Z'
    }
    decrypted_message = ""
    words = message.strip().split()
    for word in words:
        if word.capitalize() in nato_alphabet:
            decrypted_message += nato_alphabet[word.capitalize()]
        else:
            decrypted_message += word
    return decrypted_message

while True:
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted_message = nato_encrypt(message)
        print("Encrypted message: ", encrypted_message)
        break
    elif choice == 'd':
        message = input("Enter the message to decrypt: ")
        decrypted_message = nato_decrypt(message)
        print("Decrypted message: ", decrypted_message)
        break
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")
