import re

# read the file and split the string into each sequence
sequence = open(r'~/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
seq_str = sequence.read()
gene_split = re.split('>', seq_str)
# make a function to count the input end condon
def count_the_end(end_codon):
    gene_with_end_conda = [] # make an empty list to restore the required seq
    for genes in gene_split:
        genes_treated_1 = re.sub(r'\n', '', genes) # remove change line
        if re.search(end_codon, genes_treated_1): # check if there is an wanted end conda
            genes_treated_2 = re.sub(r' .+]', '\n', genes_treated_1)
            end_counter = len(re.findall(end_codon, genes_treated_2)) # count the end conda
            genes_treated_3 = re.sub(r'\n', '('+str(end_counter)+')'+'\n', genes_treated_2)
            gene_with_end_conda.append('>'+genes_treated_3) # use the list to countian the wanted seq
    output_file = open(end_codon+'_genes.fa', 'w')
    for i in gene_with_end_conda:
        output_file.write(i+'\n')


input_end_codon = input('choose one end codon(TGA, TAA, TAG):')
if input_end_codon in ['TAA', 'TAG', 'TGA']: # check the input
    count_the_end(input_end_codon)
else:
    print('wrong input')
