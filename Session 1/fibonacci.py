def fibonacci(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        n_terms = n1 + n2
        n1 = n2
        n2 = n_terms
        count += 1
    return (n2-n1)

n = int(input('Please introduce the value for the fibonacci serie: '))
fibonacci_serie = fibonacci(n)
print('Result: ',fibonacci_serie)
