def sum_of_squares(num):
    if num <= 0:
        return None

    squares = []
    for i in range(1, int(num ** 0.5) + 1):
        squares.append(i * i)

    for i in squares:
        if num - i in squares:
            return (i, num - i)
        for j in squares:
            if num - i - j in squares:
                return (i, j, num - i - j)
            for k in squares:
                if num - i - j - k in squares:
                    return (i, j, k, num - i - j - k)
    return None


for num in range(1, 20):
    result = sum_of_squares(num)
    if result:
        print(f"{num} = {'+'.join(map(str, result))}")
    else:
        print(f"Число {num} нельзя разложить на сумму не более 4 квадратов")
