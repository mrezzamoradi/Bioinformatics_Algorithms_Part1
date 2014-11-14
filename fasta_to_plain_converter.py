fileName = input()

fasta = open(fileName, 'r')
copy_filename = fileName + '_converted'

line = fasta.readline()

if line[0] == ">":
    line = line.replace('. ','_')
    line = line.replace(', ','_')
    copy_filename = line[line.index('| ') + 2:-1]
    line = fasta.readline()

plain = open(copy_filename, 'w')

while line != '':
    lineLen = len(line)
    plain.write(line[0:lineLen - 1])
    line = fasta.readline()

fasta.close()
plain.close()
