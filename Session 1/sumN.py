def sum(n):
    count = 0
    for i in range(n):
        count += i +1
    return count

n = int(input('Please introduce a number: '))
total_sum = sum(n)
print(total_sum)
