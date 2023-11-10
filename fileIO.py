filename = input()
lower_bound = input()
upper_bound = input()
file = open(f"data/{filename}")
for line in file:
    stripped = line.strip()
    print(stripped, end=" - ")
    if lower_bound <= stripped <= upper_bound:
        print("in range")
    else:
        print("not in range")

