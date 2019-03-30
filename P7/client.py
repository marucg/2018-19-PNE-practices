"""Obtaining the information of the FRAT1 gene from
    the 'rest.esembl.org'"""
import http.client
import json
from Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# OBTAINING THE DATA AND ID OF THE GENE
conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
information = json.loads(data1)
print('-- Information of the gene -- ')
print('this is info', information)
gene_id = information['data'][0]['id']
print('this is gene', gene_id)

# USING TH ID FOR GETTING THE SEQUENCE
conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/sequence/id/"+gene_id+"?content-type=application/json")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
dna = json.loads(data1)
print('this is DNA', dna)
sequence = dna['seq']
print('this is sequence', sequence)
print()

# OPERATIONS
def total_functions(seq, operation, str_seq):
    counter = seq.count(str_seq)
    if operation == 'len':
        return seq.len()
    elif operation == 'complement':
        return seq.complement()
    elif operation == 'reverse':
        return seq.reverse()
    elif operation == 'countA':
        return counter.get('A')
    elif operation == 'countC':
        return counter.get('C')
    elif operation == 'countT':
        return counter.get('T')
    elif operation == 'countG':
        return counter.get('G')
    elif operation == 'percA':
        return seq.perc('A', str_seq)
    elif operation == 'percC':
        return seq.perc('C', str_seq)
    elif operation == 'percT':
        return seq.perc('T', str_seq)
    elif operation =='percG':
        return seq.perc('G', str_seq)

s1 = Seq(sequence)
length = s1.len()
print('-- Operations -- ')
print('There are', length, 'bases in the FRAT1 gene')
count_T = total_functions(s1, 'countT', sequence)
print('There are', count_T, '"T" bases in the FRAT1 gene')
percentage = ['percA', 'percC', 'percT', 'percG']
names_bases = ['A', 'C', 'T', 'G']
for perc in percentage:
    bases = total_functions(s1, perc, sequence)
    if perc == 'percA':
        print('The percentage of A is', bases, '%')
    elif perc == 'percC':
        print('The percentage of C is', bases, '%')
    elif perc == 'percT':
        print('The percentage of T is', bases, '%')
    else:
        print('The percentage of G is', bases, '%')

perc_G = total_functions(s1, 'percG', sequence)
print('"G" is the most popular base in the FRAT1 gene with a percentage of', perc_G, '%')