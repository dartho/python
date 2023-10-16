numCount = int(input())

numbers = []
for num in range(numCount):
    numbers.append(int(input()))
    
threshold = int(input())

for num in numbers:
    if num <= threshold:
        print(num, end=" ")
