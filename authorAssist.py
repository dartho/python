def print_menu():
    print("""MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit\n""")


def get_num_of_non_WS_characters(txt):
    print("Non-ws chars")


def get_num_of_words(txt):
    print("Num words")


def fix_capitalization(txt):
    print("Fix Caps")


def replace_punctuation(txt):
    print("Replace punc")


def shorten_space(txt):
    print("Shorten space")


def execute_menu(sel, txt):
    if sel == "c":
        get_num_of_non_WS_characters(txt)
    elif sel == "w":
        get_num_of_words(txt)
    elif sel == "f":
        fix_capitalization(txt)
    elif sel == "r":
        replace_punctuation(txt)
    elif sel == "s":
        shorten_space(txt)


# Ask for text and display to user
text = input("Enter a sample text: ")
print("You entered: " + text)

# Print menu and ask for user input util a valid option is chosen
print_menu()
selection = ""
while selection not in ["c", "w", "f", "r", "s", "q"]:
    selection = input("Choose a valid option: ")

if selection != "q":
    execute_menu(selection, text)
