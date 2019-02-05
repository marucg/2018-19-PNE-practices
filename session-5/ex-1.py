def count_a(seq):
    '''Counting the numbers of As in the sequence'''
    #that is for comenting. it is necessary


    #Counter of As
    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    #return the result
    return result

#Main program
s = 'AGTGTGCAATGGCC'
number_a = count_a(s)
print('The number of As is: ',number_a)

#Calculating the length of sequence
total_length = len(s)

#Calculate the percentage of As in the sequence
percentage = round(100.0 * number_a / total_length, 1)

print('The total length is: ', total_length)
print('The percentage of As is: ', percentage)