# Testing: concatenate CDS for chromosome 1
# # (if marked + in info.gtf -- the transcript is the same as dna seq provided)

import textwrap
import sys
usage="This script is used to extract coding sequence from GTF file and genome sequences. \nUsage: python testch2.py <genome.fa> <input.gtf> > file"
if len(sys.argv)!=3:
    print (usage)
    sys.exit(usage)

# read genome sequences
chrom = open(sys.argv[1], "r")
dic = {}
c=''
for l in chrom:
    if l[0]=='>':
        c=l.split(' ')[0]
        c = c[1:]
        dic{c}=''
    else
        dic{c}+=l.strip('\n')
chrom.close()

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
    s=seq[begin-1:end]
    if(symbol == '-'):
        s=rev(s)
    return(s)

gtf = open(sys.argv[2],"r")
ptid=''
seq=''
start_flag=1
for l in gtf:
    if l[0]=='#':
        break
    else:
        words = line.split('\t')
        if words[2]=="CDS" or words[2]=="stop_codon":
            tid=words[8].split("transcript_id \"")[1]
            tid=tid.split("\"")[0]
            if tid == ptid:
                seq+=get_seq(words[0],words[3],words[4],wors[6])
            else:
                if start_flag==1:
                    break
                else:
                    print sys.stdout,">" + ptid + "\n"
                    seplist = textwrap.wrap(seq, 60)
                    print sys.stdout, '\n'.join(seplist) + "\n"
                    ptid=t
                    seq=get_seq(words[0],words[3],words[4],wors[6])

print sys.stdout,">" + ptid + "\n"
seplist = textwrap.wrap(seq, 60)
print sys.stdout, '\n'.join(seplist) + "\n"
gtf.close()


def funcneg(text):
    print ('calling funcneg()')
    print ('original: ' + text)
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

    print ('new -: ' + new)
    # return text
    return new




track_chr = ''


for line in info_notc:
    words = line.split()


    if len(words) > 5:

        chrom = words[0]
        typ = words[2]
        start = int(words[3]) - 1
        end = int(words[4]) - 1
        sign = words[6]

        # print(chrom)
        # print(typ)


        if chrom != track_chr:
            print ('change' + track_chr +'to' +chrom)
            value = ('Next' + chrom)
            s = str(value)
            print (s)#tochange

            track_chr = chrom

            lookup = '>' + str(chrom) + ' dna:chromosome'
            print ('lookup' + lookup)

            for num, linea in enumerate(lines):
                # print ('num', num)
                # print('line', line)
                if lookup in linea:
                    fil.write('\n')
                    fil.write(linea)
                    track_line = num + 1
                    print ('tag of chrom',lines[num])
                    #print 'found at line:', num
                    break


        if (typ == 'CDS' or typ =='stop_codon') and sign == "+":

            print ('found + cds')
            # fil.write('new CDS + \n')


            startline = start // 60
            startind = start % 60
            endline = end // 60
            endind = end % 60

            if endline == startline:
                first = lines[track_line + startline]
                fil.write(first[startind:endind])


            else:

                first = lines[track_line + startline]
                fil.write(first[startind:-1])
                # fil.write('\n')
                print ('firstline:' + str(first))

                i = startline + 1
                while i < endline:
                    print ('line ind' + str(i))
                    ln = lines[track_line + i]
                    fil.write(ln[:-1])
                    # fil.write('\n')
                    i += 1


                    last = lines[endline]
                    fil.write(last[:endind])
                # fil.write('\n')
                print ('lastline:' + str(last))



        elif (typ == 'CDS' or typ =='stop_codon') and sign == "-":
            print ('found - cds')
            # fil.write('new CDS - \n')

            startline = start // 60
            startind = start % 60
            endline = end // 60
            endind = end % 60


            if endline == startline:
                first = lines[track_line + startline]
                fil.write(funcneg(first[startind:endind]))



            else:


                first = lines[track_line + startline]
                first = funcneg(first)
                fil.write(first[startind:-1])
                # fil.write('\n')
                print ('firstline:' + str(first))

                i = startline + 1
                while i < endline:
                    print ('line ind'+ str(i))
                    ln = lines[track_line + i]
                    ln = funcneg(ln)
                    fil.write(ln[:-1])
                    # fil.write('\n')
                    i += 1

                    last = lines[endline]
                    last = funcneg(last)
                    fil.write(last[:endind])
                    # fil.write('\n')
                    print ('lastline:' + str(last))


info_notc.close()
chrom1.close()
fil.close()


fil2 = open("testch1.txt", "r")
filf = open('testch1res.txt',"w")
ct = 0

for lineb in fil2:

    if ct % 2 == 0:
        filf.write(lineb)

    else:
        seplist = textwrap.wrap(lineb, 60)
        print (len(seplist)) #tochange
        print (seplist[0])#tochange
        filf.write('\n'.join(seplist))
        # filf.writelines(seplist)
        # filf.writelines("%s\n" % l for l in seplist)

    ct += 1



fil2.close()
filf.close()



# def split_line(text):
#     # split the text
#     words = text.split()
#
#     # for each word in the line:
#     for word in words:
#         # print the word
#         print(word)
