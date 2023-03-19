import tkinter as tk

# Define the function to encrypt the message
def encrypt_message():
    # Get the message from the user
    message = message_entry.get()

    # Define the NATO alphabet dictionary
    nato_alphabet = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }

    # Encrypt the message
    encrypted_message = ''
    for letter in message:
        if letter.upper() in nato_alphabet:
            encrypted_message += nato_alphabet[letter.upper()] + ' '
        else:
            encrypted_message += letter

    # Update the label with the encrypted message
    encrypted_message_label.config(text='Encrypted message: ' + encrypted_message)


# Create the GUI window
window = tk.Tk()
window.title('NATO Alphabet Encryption')

# Create the message label and entry widget
message_label = tk.Label(window, text='Enter message:')
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

# Create the button to encrypt the message
encrypt_button = tk.Button(window, text='Encrypt', command=encrypt_message)
encrypt_button.pack()

# Create the label to display the encrypted message
encrypted_message_label = tk.Label(window, text='Encrypted message: ')
encrypted_message_label.pack()

# Run the GUI
window.mainloop()
