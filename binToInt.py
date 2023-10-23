def bin_to_int(str_val):
    rev_str = reverse_string(str_val)
    int_val = 0
    for e in range(len(rev_str)):
        if int(rev_str[e]) == 1:
            int_val += 2**e
    return int_val


def reverse_string(str_val):
    return str_val[::-1]


my_bin = input("Enter a binary string: ")
print(f"{bin_to_int(my_bin)} = {my_bin}")
