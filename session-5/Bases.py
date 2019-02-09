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

