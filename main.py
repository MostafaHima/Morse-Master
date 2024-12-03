# Morse Code Dictionary
morse_code_dict = {
    "A": "•-", "B": "-•••", "C": "-•-•", "D": "-••", "E": "•", "F": "••-•", "G": "--•", "H": "••••", "I": "••",
    "J": "•---", "K": "-•-", "L": "•-••", "M": "--", "N": "-•", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", "/": "-..-.", "!": "-.-.--", "@": ".--.-.", "&": ".-...", "(": "-.--.",
    ")": "-.--.-", "+": ".-.-.", "=": "-...-", '"': ".-..-.", ":": "---...", "'": ".----.",
    ",": "--..--"
}

# Lists to store valid and invalid characters
valid_morse = []  # List for characters that can be converted to Morse Code
invalid_characters = []  # List for characters not in the Morse dictionary

# Strings to hold final outputs
morse_output = ""  # Final Morse code output
invalid_output = ""  # List of invalid characters as a string

# Taking user input
user_input = input("Write your text here without spaces: ")

# Check each character in the input
for char in user_input.upper():
    if char in morse_code_dict:  # If character is in Morse dictionary
        valid_morse.append(morse_code_dict[char])
    else:  # If character is not in Morse dictionary
        invalid_characters.append(char)

# Handle output based on validity
if len(invalid_characters) == 0:  # If no invalid characters exist
    for morse_char in valid_morse:
        morse_output += f"{morse_char} "

    print("Morse Code Translation:")
    print("=========================================================================================================\n")
    print(morse_output)
    print("\n=========================================================================================================")


else:  # If there are invalid characters
    for invalid_char in invalid_characters:
        invalid_output += f"{invalid_char} "

    print("=========================================================================================================\n")
    print("The following characters could not be converted to Morse Code:")
    print(invalid_output)
    print("\n=========================================================================================================")


