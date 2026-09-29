import sys
import string


def sumUpperCharacters(phrase: str) -> int:
    """Counts and returns the total number of uppercase letters in a string."""
    count = 0
    for letter in phrase:
        if letter.isupper():
            count += 1
    return count


def sumLowerCharacters(phrase: str) -> int:
    """Counts and returns the total number of lowercase letters in a string."""
    count = 0
    for letter in phrase:
        if letter.islower():
            count += 1
    return count


def sumPunctuationMarks(phrase: str) -> int:
    """Counts and returns the total number of punctuation marks in a string."""
    count = 0
    for letter in phrase:
        if letter in string.punctuation:
            count += 1
    return count


def sumSpaces(phrase: str) -> int:
    """Counts and returns the total number of space
    characters (spaces, tabs, newlines) in a string."""
    count = 0
    for letter in phrase:
        if letter.isspace():
            count += 1
    return count


def sumDigits(phrase: str) -> int:
    """Counts and returns the total number of digits (0-9) in a string."""
    count = 0
    for letter in phrase:
        if letter.isdigit():
            count += 1
    return count


def generateOutput(phrase: str) -> None:
    """Calculates all statistics for the text and
    prints the formatted results."""
    print(f"The text contains {len(phrase)} characters:")
    print(f"{sumUpperCharacters(phrase)} upper letters")
    print(f"{sumLowerCharacters(phrase)} lower letters")
    print(f"{sumPunctuationMarks(phrase)} punctuation marks")
    print(f"{sumSpaces(phrase)} spaces")
    print(f"{sumDigits(phrase)} digits")


def main():
    """Validates command-line arguments and triggers
    the text analysis process."""
    argv = sys.argv

    if len(argv) > 2:
        raise AssertionError("More than one argument")

    if len(argv) == 1:
        print("What is the text to count?")
        question = sys.stdin.read()
        generateOutput(question)
    elif len(argv) == 2:
        generateOutput(argv)


if __name__ == "__main__":
    main()
