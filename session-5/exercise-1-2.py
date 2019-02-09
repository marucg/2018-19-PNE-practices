from Bases import count_bases

#MAIN PROGRAM
s = input('Please enter the sequence: ').upper()
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

