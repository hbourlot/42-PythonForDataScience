import sys

if len(sys.argv) > 1:

    parsed_input = sys.argv[1:]

    if len(parsed_input) == 1:
        value = int(parsed_input[0])
        print(f"{"I'm Even" if ((value % 2) == 0) else "I'm Odd"}.")
    else:
        print("AssertionError: ")
        if len(parsed_input):
            print("more than one argument is provided")
        else:
            print("argument is not an integer")
