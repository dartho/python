def int_to_bin(int_val):
    bin_str = ""
    while int_val > 0:
        bit = int_val % 2
        bin_str += str(bit)
        int_val = int_val // 2
    return reverse_string(bin_str)


def reverse_string(str_val):
    return str_val[::-1]


my_int = int(input())
print(f"{my_int} = {int_to_bin(my_int)}")
