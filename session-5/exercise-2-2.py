from Bases import count_bases

def percentage(base):
    specific_base = total_bases.get(base)
    if total_length > 0:
        percentage = round(100.0 * specific_base / total_length, 1)
    else:
        percentage = 0
    print('Base', base, '\n\tCounter: ', specific_base, '\n\tPercentage: ', percentage)

#OBTAINING SEQUENCES AND MAKING LIST
s1 = input('Please enter the sequence 1: ').upper()
s2 = input('Please enter the sequence 2: ').upper()
list_s = [s1,s2]

#GETTING ELEMENTS FROM LIST OF SEQUENCES
number_seq = 0
for position in list_s:
    number_seq += 1
    total_length = len(position)
    print('\nSequence',number_seq,'is',total_length,'bases in length')
    total_bases = count_bases(position)
    percentage('A')
    percentage('C')
    percentage('G')
    percentage('T')
