class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        seq = ''
        for base in self.strbases:
            if base == 'A':
                seq += dictionary.get('A')
            elif base == 'C':
                seq += dictionary.get('C')
            elif base == 'T':
                seq += dictionary.get('T')
            else:
                seq += dictionary.get('G')
        return seq

    def reverse(self):
        return self.strbases[::-1]

    def count(self,base):
        count_a = count_c = count_g = count_t = 0
        for b in base:
            if b == 'A':
                count_a += 1
            elif b == 'C':
                count_c += 1
            elif b == 'G':
                count_g += 1
            elif b == 'T':
                count_t += 1
        dictionary = {'A': count_a, 'C': count_c, 'G': count_g, 'T': count_t}
        return dictionary


    def perc(self,base,total_length):
        if total_length > 0:
            percentage = round(100.0 * base / total_length, 1)
        else:
            percentage = 0
        return percentage


