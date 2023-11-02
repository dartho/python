def fractal(length, spaces):
    if length > 0:
        if length == 1:
            # last line
            print_span(" ", spaces)
            print("*")
        else:
            half_length = int(length//2)
            # top
            fractal(half_length, spaces)

            # middle
            print_span(" ", spaces)
            print_span("*", length)
            print()  # new line

            # bottom
            fractal(half_length, spaces + half_length)


def print_span(char, num):
    for i in range(num):
        print(char, end="")


fractal(4, 0)
