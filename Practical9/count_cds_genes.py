import re
import os


end_codon = input('choose one end codon(TGA, TAA, TAG):')

os.chdir('C:/cygwin64/home/10755/IBI1_2022-23/Practical9/')
sequence = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
seq_str = sequence.read()
gene_split = re.split('>',seq_str)
gene_with_end_conda = []
for i in gene_split:
    m = re.sub(r'\n', '', i)
    if re.search(end_codon+'$', m):
        h = re.sub(r' .+]', '\n', m)
        gene_with_end_conda.append('>'+h)
count = len(gene_with_end_conda)
output_file = open(end_codon+'_genes.fa', 'w')
output_file.write('There are '+str(count)+' genes end with \''+end_codon+'\'.\n')
for i in gene_with_end_conda:
    output_file.write(i+'\n')
