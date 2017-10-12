#Testing: concatenate CDS for chromosome 1
# # (if marked + in info.gtf -- the transcript is the same as dna seq provided)

import textwrap
import sys
usage = "This script is used to extract coding sequence from GTF file and genome sequences. \nUsage: python testch2.py <genome.fa> <input.gtf> > file"

if len(sys.argv) != 3:
    print (usage)
    sys.exit(usage)


# read genome sequences
print sys.stderr, "read genom... \n"
chrom = open(sys.argv[1], "r")

dic = {}
c =' '
ct = 0;
temstr=''

for l in chrom:
    # print sys.stderr, ct
    ct += 1

    if l[0] == '>':
        # c = l.split(' ')[0]
        # c = c[1:]
        print sys.stderr, "new c\n" + c
        # dic[c] = ''
    
    else:
        #comment
        temstr += l.strip('\n')
        #print sys.stderr, temstr[:300]
    	#print sys.stderr, l.strip('\n')
    	#print sys.stderr, "dic section\n" + dic[c][:100]
    	# print sys.stderr, "dic" + dic[c]

chrom.close()







print sys.stderr, "read gtf ...\n"
