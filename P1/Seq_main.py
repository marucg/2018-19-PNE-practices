from Seq import Seq

s1 = Seq('ACTGTGTGCCA')
s2 = Seq('ACTGT')
s3 = s1.complement()
s3_converted = Seq(s3)
s4 = s3_converted.reverse()
# GETTING SEQUENCES
str1 = s1.strbases
str2 = s2.strbases
str3 = s3
str4 = s4
list_str = [str1, str2, str3, str4]


count = 0
for position in list_str:
    count += 1
    total_length = len(position)
    print('\nSequence', count,':', position,'\n\tLength:', total_length)
    counter = s1.count(position)
    print('\tBases count: A:',counter.get('A'),', T:',counter.get('T'),', C:',counter.get('C'),', G:',counter.get('G'))
    list_bases = ['A','T','C','G']
    total_perc = []
    for base in list_bases:
        total_bases = counter.get(base)
        percentage = s1.perc(total_bases,total_length)
        total_perc.append(percentage)
    print('\tBases percentage: A:',total_perc[0],'%, T:',total_perc[1],'%, C:',total_perc[2],'%, G:',total_perc[3],'%')
