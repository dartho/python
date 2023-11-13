# create an output directory if it doesn't exist
from pathlib import Path
Path("output").mkdir(parents=True, exist_ok=True)

# ask for input file name
try:
    file_name = input()
    file = open(f"data/{file_name}")
except FileNotFoundError as err:
    print("Error: Bad File Name")
    exit(0)

# init dict/list
shows = {}
titles = []

# for each line(key)/line + 1(value) pair, add to dictionary
lines = file.readlines()
for i in range(0, len(lines), 2):
    key = int(lines[i].strip())
    value = lines[i + 1].strip()
    titles.append(value)
    if key in shows.keys():
        existing_value = shows[key]
        shows.update({key: f"{existing_value}; {value}"})
    else:
        shows.update({key: value})
file.close()

# reverse the dictionary by key and write out to file
keys_reversed = dict(sorted(shows.items(), reverse=True))
output_keys = []
for key in keys_reversed.keys():
    output_keys.append(f"{key}: {keys_reversed[key]}")
out_file = open("output/output_keys.txt", "w")
out_file.writelines("\n".join(output_keys))
out_file.close()

# reverse the list and write out to file
titles.sort(reverse=True)
out_file = open("output/output_titles.txt", "w")
out_file.write("\n".join(titles))
out_file.close()
