phrase = input()

words = phrase.split()
word_dict = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_dict:
        word_count = word_dict.get(word_lower)
        word_dict.update({word_lower: word_count + 1})
    else:
        word_dict.update({word_lower: 1})

for word in words:
    print(f"{word} {word_dict[word.lower()]}")
