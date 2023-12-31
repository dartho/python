def print_menu():
    print("""MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit\n""")


def get_num_of_non_WS_characters(txt):
    print("Num of non-WS chars")


def get_num_of_words(txt):
    print("Num of words")


def fix_capitalization(txt):
    print("Fix caps")


def replace_punctuation(txt, exclamation_count=0, semicolon_count=0):
    print("Punctuation replaced")


def shorten_space(txt):
    print("Shorten spaces")


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
print(f"\nYou entered: {text}\n")

# Print menu and ask for user input util a valid option is chosen
print_menu()
selection = ""
while selection not in ["c", "w", "f", "r", "s", "q"]:
    selection = input("Choose a valid option: ")

# If user chose "q", just exit program, otherwise execute menu selection
if selection != "q":
    execute_menu(selection, text)
