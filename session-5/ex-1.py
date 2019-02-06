#when i press enter without typing any sequence
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
s = 'ACTGTGTCAACC'
number_a = count_a(s)
print('The number of As is: ',number_a)

#Calculating the length of sequence
total_length = len(s)

#Calculate the percentage of As in the sequence
if total_length > 0:
    percentage = round(100.0 * number_a / total_length, 1)
else:
    percentage = 0

print('The total length is: ', total_length)
print('The percentage of As is: ', percentage)

#ALWAYS bug, it will lead me to the error
#For functions click the second botton