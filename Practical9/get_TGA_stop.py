import re
import os

os.chdir('C:/cygwin64/home/10755/IBI1_2022-23/Practical9/')
# open the sequence file for read, read the entire file as a string
sequence = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
seq_str = sequence.read()
# split the string by genes
gene_split = re.split('>',seq_str)
gene_with_TGA = []
# find the gene that have the end codon TGA, collect them in a list
for i in gene_split:
    m = re.sub(r'\n', '', i)
    if re.search('TGA$', m):
        h = re.sub(r' .+]', '\n', m)
        gene_with_TGA.append('>'+h)
# write an out put file
output_file = open('TGA_genes.fa', 'w')
for i in gene_with_TGA:
    output_file.write(i+'\n')
