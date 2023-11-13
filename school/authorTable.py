"""
Number of Novels Authored
Author name
Number of novels
Jane Austen, 6
Charles Dickens, 20
Ernest Hemingway, 9
Jack Kerouac, 22
F. Scott Fitzgerald, 8
Mary Shelley, 7
Charlotte Bronte, 5
Mark Twain, 11
Agatha Christie, 73
Ian Flemming, 14
Stephen King, 54
Oscar Wilde, 1
-1

"""

def validate_data(string):
    split_string = string.split(",")
    if len(split_string) == 1:
        return "No comma in string."
    elif len(split_string) > 2:
        return "Too many commas in input."
    elif not split_string[1].strip().isdigit():
        return "Comma not followed by an integer."
    return ""


# output in table format: title min 33 right just, col 1 min 20 left just, col 2 min 23 right just
def output_table(label, col1_name, col2_name, author_list):
    col1_max_string_length = 0
    for author in author_list:
        name = author.get("col1")
        if len(name) > col1_max_string_length:
            col1_max_string_length = len(name)

    col1_length = 20 if col1_max_string_length < 20 else col1_max_string_length
    col2_length = 23
    combined_width = col1_length + col2_length + 1

    print(pad_string(label, " ", 33, "right"))

    c1_header = pad_string(col1_name, " ", col1_length, "left")
    c2_header = pad_string(col2_name, " ", col2_length, "right")
    print(f"{c1_header}|{c2_header}")

    print(pad("-", combined_width))

    for author in author_list:
        name = author.get("col1")
        num_books = author.get("col2")
        c1_data = pad_string(name, " ", col1_length, "left")
        c2_data = pad_string(str(num_books), " ", col2_length, "right")
        print(f"{c1_data}|{c2_data}")


# output histogram with name min 20 right just, num stars for values
def output_histogram(author_list):
    for author in authors:
        name = author.get("col1")
        num_books = author.get("col2")
        s1 = pad_string(name, " ", 20, "right")
        s2 = pad("*", num_books)
        print(f"{s1} {s2}")


def pad(char, num):
    return char * num


def pad_string(string, pad_char, min_length, justify):
    length = min_length if len(string) <= min_length else len(string)
    if justify == "right":
        return f"{pad(pad_char, length - len(string))}{string}"
    else:
        return f"{string}{pad(pad_char, length - len(string))}"


# Enter title for data
title = input("Enter a title for the data:\n")
print(f"You entered: {title}\n")

# enter column header 1
col1_header = input("Enter the column 1 header:\n")
print(f"You entered: {col1_header}\n")

# enter column header 2
col2_header = input("Enter the column 2 header:\n")
print(f"You entered: {col2_header}\n")


# LOOP
row = ""
authors = []
while row != "-1":
    # enter row of data (str, int), -1 to stop input
    row = input("Enter a data point (-1 to stop input):\n")
    if row.strip() != "-1":
        # check data for errors:
        error = validate_data(row)
        if error:
            print(f"Error: {error}\n")
        else:
            row_data = row.split(",")
            col1_data = row_data[0].strip()
            col2_data = int(row_data[1])
            authors.append({"col1": col1_data,
                           "col2": col2_data})
            print(f"Data string: {col1_data}")
            print(f"Data integer: {col2_data}\n")

if len(authors) > 0:
    print()
    output_table(title, col1_header, col2_header, authors)
    print()
    output_histogram(authors)
