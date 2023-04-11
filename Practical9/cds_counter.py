import re

def counter(seq):
    # check the sequence whether is valid
    for i in seq:
        if i not in ['A', 'C', 'T', 'G']:
            return 'this is not a valid sequence'
    # use re to search for the ending codon
    result = re.findall('(TAA)|(TAG)|(TGA)', seq)
    count = len(result)
    return count

print(counter('ATGCAATCGACTACGATCTGAGAGGGCCTAA'))
