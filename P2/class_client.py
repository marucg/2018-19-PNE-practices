# Class that i'll use for converting the sequence of the user
# Making def complement() and reverse()
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

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
