def fibonnaci(length: int):
    if length == 2 or length == 1:
        return 1
    else:
        return fibonnaci(length - 1) + fibonnaci(length - 2)

for i in range(1,21):
    print(fibonnaci(i))