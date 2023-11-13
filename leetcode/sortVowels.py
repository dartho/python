# https://leetcode.com/problems/sort-vowels-in-a-string

def sortVowels(s) -> str:
    v_list = []
    v_index = []
    sorted_str = []
    for i in range(len(s)):
        letter = s[i]
        sorted_str.append(letter)
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            v_list.append(letter)
            v_index.append(i)
    v_list.sort()
    for i in range(len(v_index)):
        sorted_str[v_index[i]] = v_list[i]
    return "".join(sorted_str)


print(sortVowels("lEetcOde"))
print(sortVowels("lYmph"))
