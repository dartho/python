x1, y1, s1, x2, y2, s2 = input("Enter values separated by a space: ").split()
#8 7 38 3 -5 -1

solution = []
exitLoop = False
x = -10
while -10 <= x <= 10 and not exitLoop:
    y = -10
    while -10 <= y <= 10 and not exitLoop:
        if (int(x1) * x) + (int(y1) * y) == int(s1) and (int(x2) * x) + (int(y2) * y) == int(s2):
            solution.append(x)
            solution.append(y)
            exitLoop = True
        y += 1
    x += 1

if len(solution) > 0:
    print(f"x = {solution[0]} , y = {solution[1]}")
else:
    print("There is no solution")
