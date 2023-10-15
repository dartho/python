terminators = ["Done", "done", "d"]
output = []
run = True
while run:
    phrase = input("Enter your phrase: ")
    if phrase not in terminators:
        '''
        # Manually reverse string
        phraseOut = ""
        phraseLength = len(phrase)
        for x in range(0, phraseLength):
            currIndex = (phraseLength - 1) - x
            phraseOut += phrase[currIndex]
            output.append(phraseOut)
        '''
        output.append(phrase[::-1])
    else:
        run = False

for phrase in output:
    print(phrase)