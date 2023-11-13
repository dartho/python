print("Welcome to a fun word replacement game.")
try:
    print("Enter the name of the file to use:")
    file_name = input()
    file = open(f"data/{file_name}")
except FileNotFoundError as err:
    print("Error: Bad File Name")
    exit(0)

new_lines = []
vowels = ["a", "e", "i", "o", "u"]
for line in file:
    words = line.split()
    for i in range(len(words)):
        word = words[i]
        if word.startswith("["):
            word_type = word[word.index("[") + 1: word.index("]")]
            a_an = "an" if word_type[0] in vowels else "a"
            new_word = ""
            while not new_word:
                print("Please give", a_an, word_type.replace("-", " "))
                new_word = input()
            words[i] = words[i].replace(f"[{word_type}]", new_word)
    new_lines.append(words)

print("Here is your story:")
print("--------------------")
for line in new_lines:
    print(" ".join(line))
