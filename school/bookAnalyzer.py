INVALID_FILE = "Error: Could Not Open File."
INVALID_ALPHA = "Error: A single letter is required."
INVALID_NUMBER = "Error: A number is required."

print("Welcome to Book Analyzer v0.1")
try:
    # prompt for file name and open
    file_name = input("Enter File Name to Read:\n")
    file = open(f"data/{file_name}")

    # prompt for letter to search for
    letter = input("Letter to search for:\n")
    if not letter.isalpha() or len(letter) > 1:
        raise Exception(INVALID_ALPHA)

    # prompt for position
    position = int(input("Enter Position (0 for first letter):\n"))
    if position < 0:
        raise Exception(INVALID_NUMBER)

    counter = 0
    for line in file:
        words = line.split()
        for word in words:
            if position < len(word) and word[position].lower() == letter.lower():
                counter += 1

    print(f"There are {counter} words with {letter} in position {position}")

except FileNotFoundError as err:
    print(INVALID_FILE)
except ValueError as err:
    print(INVALID_NUMBER)
except Exception as err:
    print(err)
