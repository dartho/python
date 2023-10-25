# test string: hello world.    how are you? i'm doing fine!   that's nice. let's test; string replacement!!

def print_menu():
    print("""MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit\n""")


def get_num_of_non_WS_characters(txt):
    counter = 0
    for c in txt:
        if not c.isspace():
            counter += 1
    print(f"Number of non-whitespace characters: {counter}")


def get_num_of_words(txt):
    split_txt = txt.split()
    print(f"Number of words: {len(split_txt)}")


def fix_capitalization(txt):
    cap_text = split_and_cap_by_delimiter(txt, ".")
    cap_text = split_and_cap_by_delimiter(cap_text[0], "!", cap_text[1])
    cap_text = split_and_cap_by_delimiter(cap_text[0], "?", cap_text[1])
    print(f"Number of letters capitalized: {cap_text[1]}")
    print(f"Edited text: {cap_text[0]}")


def split_and_cap_by_delimiter(txt, delimiter, counter=0):
    split_txt = txt.split(delimiter)
    for i in range(len(split_txt)):
        sentence = split_txt[i]
        partial = ""
        for c in range(len(sentence)):
            character = sentence[c]
            if not character.isspace():
                if character.islower():
                    sentence = sentence[c].capitalize() + sentence[c+1:]
                    counter += 1
                break
            else:
                partial += character
        split_txt[i] = partial + sentence
    return delimiter.join(split_txt), counter


def replace_punctuation(txt, exclamation_count=0, semicolon_count=0):
    new_txt = ""
    for i in range(len(txt)):
        if txt[i] == "!":
            new_txt += "."
            exclamation_count += 1
        elif txt[i] == ";":
            new_txt += ","
            semicolon_count += 1
        else:
            new_txt += txt[i]
    print("Punctuation replaced")
    print(f"exclamation_count: {exclamation_count}")
    print(f"semicolon_count: {semicolon_count}")
    print(f"Edited text: {new_txt}")


def shorten_space(txt):
    split_txt = txt.split()
    print(f"Edited text: {' '.join(split_txt)}")


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
