def max_magnitude(vals):
    sign = 1
    max_value = 0
    for value in vals:
        if abs(value) > max_value:
            max_value = abs(value)
            sign = -1 if value < 0 else 1
    return max_value * sign


def max_mag_alt(val1, val2, val3):
    aval1 = abs(val1)
    aval2 = abs(val2)
    aval3 = abs(val3)
    val_dict = {aval1: (val1 < 0),
                aval2: (val2 < 0),
                aval3: (val3 < 0)}
    max_val = max(aval1, aval2, aval3)
    sign = -1 if val_dict[max_val] else 1
    return max(aval1, aval2, aval3) * sign


values = [int(input()), int(input()), int(input())]
max_mag = max_magnitude(values)

#v1 = int(input())
#v2 = int(input())
#v3 = int(input())
#max_mag = max_mag_alt(v1, v2, v3)

print(max_mag)


