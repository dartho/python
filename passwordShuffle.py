passwordIn = input("Enter your password: ")
altLetters = {"a": "@", "E": "3", "e": "3", "i": "!",
              "I": "1", "o": "0", "O": "0", "u": "U",
              "y": "4", "Y": "4"}

passwordOut = ""
for letter in passwordIn:
    if letter in altLetters:
        passwordOut += altLetters[letter]
    else:
        passwordOut += letter

print("Original password: " + passwordIn)
print("New password: " + passwordOut)
