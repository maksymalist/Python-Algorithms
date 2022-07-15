def main(n, result):
    if n == 1:
        return result
    return main(n-1, n*result)

factorial = main(5, 1)


print(factorial)