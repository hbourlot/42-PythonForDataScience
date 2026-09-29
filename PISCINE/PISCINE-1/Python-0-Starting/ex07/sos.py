import sys

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
        exit(1)

    phrase = argv[1]

    if not phrase:
        print("")
        exit(0)

    morse_message = []

    for letter in phrase:
        upper_letter = letter.upper()

        if upper_letter in NESTED_MORSE and (
            upper_letter.isalnum() or upper_letter == " "
        ):
            morse_message.append(NESTED_MORSE[upper_letter])
        else:
            print("AssertionError: the arguments are bad")
            exit(1)

    print(" ".join(morse_message))
