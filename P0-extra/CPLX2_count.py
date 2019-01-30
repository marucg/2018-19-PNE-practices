def load_data(file):
    f = open(file, 'r')
    info = f.read()
    line = info.find('\n')
    new_line = info[line+1:]
    final_line = new_line.replace('\n','')
    return final_line
#Changing load_data
line_info = load_data('CPLX2.txt')

def codons_genome(a,c,t,g):
    A_count = line_info.count(a)
    C_count = line_info.count(c)
    T_count = line_info.count(t)
    G_count = line_info.count(g)
    print('A:',A_count,'\nC:',C_count,'\nT:',T_count,'\nG:',G_count)

#Counting
codons_genome('A','C','T','G')
