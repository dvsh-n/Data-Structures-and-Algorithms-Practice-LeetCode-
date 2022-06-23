def factorial(num: int):
    if num == 2:
        return num
    return num * factorial(num - 1)

print(factorial(5))