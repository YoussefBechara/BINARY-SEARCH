list = [1, 4, 8, 9, 32, 46, 95, 23]
def binary_searh():
    lower = 0
    upper = len(list) - 1
    n = 0
    while lower <= upper:
        mid = (lower + upper) // 2
        if n > mid:
            lower = mid
        elif n < mid:
            upper = mid
        else:
            print(list[n])
            break

binary_searh()
