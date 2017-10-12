# Testing: concatenate CDS for chromosome 1
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

for l in chrom:

    if l[0] == '>':
        c = l.split(' ')[0]
        c = c[1:]
        print sys.stderr, "new c\n" + c
        dic[c] = ''

    else:
        dic[c] += l.strip('\n')
        print sys.stderr, l.strip('\n')
        print sys.stderr, "dic section\n" + dic[c][:1000]
        # print sys.stderr, "dic" + dic[c]

chrom.close()



print sys.stderr, "read gtf ...\n"

def rev(text):
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

    if l[0] == '#':
        break

    else:
        words = line.split('\t')

        if words[2] == "CDS" or words[2] == "stop_codon":
            print sys.stderr, "found new CDS/codon"

            tid = words[8].split("transcript_id \"")[1]
            tid = tid.split("\"")[0]

            if tid == ptid:
                seq += get_seq(words[0], words[3], words[4], words[6])

            elif start_flag == 1:
                print sys.stderr,"first"
                start_flag = 0

            else:
                print sys.stdout,">" + ptid + "\n"
                seplist = textwrap.wrap(seq, 60)
                print sys.stdout, '\n'.join(seplist) + "\n"

                print sys.stderr, "new ptid"
                ptid = tid
                seq = get_seq(words[0], words[3], words[4],words[6])


print sys.stdout,">" + ptid + "\n"
seplist = textwrap.wrap(seq, 60)
print sys.stdout, '\n'.join(seplist) + "\n"

gtf.close()
