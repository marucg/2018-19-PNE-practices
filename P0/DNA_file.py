with open('DNA_file.txt','r') as f:
    line = f.read()
    line = line.replace('\n','')
    print(line)
    f.close()
    length = len(line)
    print('The length of the chain: ',length)
    A_count = line.count('A')
    C_count = line.count('C')
    T_count = line.count('T')
    G_count = line.count('G')
    print('A:',A_count,'\nC:',C_count,'\nT:',T_count,'\nG:',G_count)


