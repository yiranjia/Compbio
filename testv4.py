# Testing: concatenate CDS for chromosome 1
# # (if marked + in info.gtf -- the transcript is the same as dna seq provided)

import textwrap
import sys
usage = "This script is used to extract coding sequence from GTF file and genome sequences. \nUsage: python testch2.py <genome.fa> <input.gtf> > file"

if len(sys.argv) != 3:
    print (usage)
    sys.exit(usage)


# read genome sequences
print >> sys.stderr, "read genom... \n"
chrom = open(sys.argv[1], "r")

dic = {}
c = ''
ct = 0;
start = 1

for l in chrom:
    # print sys.stderr, ct
    ct += 1

    if 'CHR' in l[0:5]:
    	break

    if l[0] == '>':

        if start == 1:
            c = l.split(' ')[0]
            c = c[1:]
            print >> sys.stderr, "new c\n" + c
            temstr = ''
            start = 0


        else:
            dic[c] = temstr
            c = l.split(' ')[0]
            c = c[1:]
            print >> sys.stderr, "new c\n" + c
            temstr = ''
    
    else:
        #comment
        temstr += l.strip('\n')
    	#print sys.stderr, l.strip('\n')
    	#print sys.stderr, "dic section\n" + dic[c][:100]
    	# print sys.stderr, "dic" + dic[c]


dic[c] = temstr

chrom.close()







print >> sys.stderr, "read gtf ...\n"

def rev(text):

    new = ''

    for a in text:
        if a == 'A':
            new += 'T'
        elif a == 'T':
        	new += 'A'
    	elif a == 'G':
        	new += 'C'
        elif a == 'C':
            new += 'G'
    	else:
            new += a
    return new[::-1]


def get_seq(chro, begin, end, symbol):
    seq = dic[chro]
    begin = int(begin)
    end = int(end)

    s = seq[begin-1:end]

    if (symbol == '-'):
        s = rev(s)
    
    return(s)







gtf = open(sys.argv[2],"r")

ptid = ''
seq = ''
start_flag = 1

for line in gtf:

    words = line.split('\t')

    if line[0] != '#' and (words[2] == "CDS" or words[2] == "stop_codon"):
        #comment
        
        # print sys.stderr, words[0]
        # print sys.stderr, words[1]	

        #print sys.stderr, "found new CDS/codon"

        #print sys.stderr, words[8]
        tid = words[8].split("transcript_id \"")[1]
        tid = tid.split("\"")[0]

        if tid == ptid:
        	seq += get_seq(words[0], words[3], words[4], words[6])

        elif start_flag == 1:
            #print sys.stderr,"first"
            start_flag = 0
            ptid = tid
            seq = get_seq(words[0], words[3], words[4],words[6])
        
        else:
            print >> sys.stdout,">" + ptid + "\n"
            seplist = textwrap.wrap(seq, 60)
            print >> sys.stdout, '\n'.join(seplist) + "\n"

            print >> sys.stderr, "new ptid" + tid
            ptid = tid
            seq = get_seq(words[0], words[3], words[4],words[6])


print >> sys.stdout,">" + ptid + "\n"
seplist = textwrap.wrap(seq, 60)
print >> sys.stdout, '\n'.join(seplist) + "\n"

gtf.close()
