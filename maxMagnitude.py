def max_magnitude(vals):
    sign = 1
    max_value = 0
    for value in vals:
        if abs(value) > max_value:
            max_value = abs(value)
            sign = -1 if value < 0 else 1
    return max_value * sign


values = [int(input()), int(input()), int(input())]

max_mag = max_magnitude(values)
print(max_mag)
