filename = input()
lower_bound = input()
upper_bound = input()
file = open(f"data/{filename}")
for line in file:
    stripped = line.strip()
    if lower_bound <= stripped <= upper_bound:
        print(stripped, "- in range")
    else:
        print(stripped, "- not in range")

