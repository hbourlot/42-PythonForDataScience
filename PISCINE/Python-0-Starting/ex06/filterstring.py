import sys

if __name__ == "__main__":

    argv = sys.argv

    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        exit(1)

    second_parameter = 0

    if argv[2].isnumeric():
        second_parameter = int(argv[2])
    else:
        print("AssertionError: the arguments are bad")
        exit(1)

    first_parameter = argv[1].split()

    result = []

    for word in first_parameter:
        if len(word) >= second_parameter:
            result.append(word)

    print(result)
