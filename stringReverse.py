terminators = ["Done", "done", "d"]
output = []
run = True
while run:
    phrase = input("Enter your phrase: ")
    if phrase not in terminators:
        phraseOut = ""
        phraseLength = len(phrase)
        for x in range(0, phraseLength):
            currIndex = (phraseLength - 1) - x
            phraseOut += phrase[currIndex]
        output.append(phraseOut)
    else:
        run = False

for phrase in output:
    print(phrase)