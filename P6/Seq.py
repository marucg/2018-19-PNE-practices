'''File containing the functions for the server'''
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

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


    def perc(self,base, seq):
        counter = self.count(seq)
        counter = counter.get(base)
        percentage = round(100.0 * counter / self.len(), 1)
        return percentage
