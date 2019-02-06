def count_bases(seq):
    '''Counting the numbers of As in the sequence'''
    count_a = count_c = count_g = count_t = 0
    for b in seq:
        if b == 'A':
            count_a += 1
        elif b == 'C':
            count_c += 1
        elif b == 'G':
            count_g += 1
        elif b == 'T':
            count_t += 1
    dictionary = {'A':count_a,'C':count_c,'G':count_g,'T':count_t}
    return dictionary

#Main program
s = input('Please enter the sequence: ')
s = s.upper()
total_bases = count_bases(s)
#Calculating the length of sequence
total_length = len(s)
print('The total length of the sequence is: ', total_length)

def percentage(base):
    specific_base = total_bases.get(base)
    if total_length > 0:
        percentage = round(100.0 * specific_base / total_length, 1)
    else:
        percentage = 0
    print('Base', base, '\n\tCounter: ', specific_base, '\n\tPercentage: ', percentage)

#calling function
percentage('A')
percentage('C')
percentage('G')
percentage('T')

