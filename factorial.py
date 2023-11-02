def factorial_recursion(num):
    if num - 1 > 0:
        return num * factorial_recursion(num - 1)
    else:
        return num


def factorial_for(num):
    product = 1
    for i in range(num):
        product *= i + 1
    return product


def factorial_while(num):
    i = num
    product = 1
    while i > 0:
        product *= i
        i -= 1
    return product


f = 5
print(factorial_recursion(f))
print(factorial_for(f))
print(factorial_while(f))


