def factorial_recursion(num):
    return num * factorial_recursion(num - 1) if num - 1 > 0 else num


def factorial_recursion_exp(num):
    if num - 1 > 0:
        return num * factorial_recursion_exp(num - 1)
    else:
        return num


def factorial_for(num):
    product = 1
    for i in range(num):
        product *= i + 1
    return product


def factorial_while(num):
    product = 1
    while num > 0:
        product *= num
        num -= 1
    return product


f = 5
print(factorial_recursion(f))
print(factorial_recursion_exp(f))
print(factorial_for(f))
print(factorial_while(f))
