import re


def cap(string):
    return re.search(p, string).group(1).capitalize()


p = re.compile(r'((?<=[\.\?!]\s)(\w+)|(^\s*\w+))')
txt = "      hello world.  how are you."
s = re.sub(p, cap(txt), txt)
print(s)

