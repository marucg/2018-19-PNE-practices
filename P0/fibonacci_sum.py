def fibonacci(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        if count < (n-1):
            print(n1, end=',')
        elif count < n:
            print(n1)
        n_terms = n1 + n2
        n1 = n2
        n2 = n_terms
        count += 1

n = int(input('Please introduce the value for the fibonacci serie: '))
print('The sum of the terms of the fibonacci serie is: ')
fibonacci_serie = fibonacci(n)
fibonacci_serie

