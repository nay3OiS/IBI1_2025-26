# Given DNA sequence as required
seq = 'ATGCAGAATTCAGTGGTGTGTCTGTTGAATTCCTGAGAGGGCCTAA'
cut_site = 'GAATTC'
# count how many EcoRI cut sites
cut_count = seq.count(cut_site)
# linear DNA: fragments = cut_site + 1
fragment_total = cut_count + 1
# print the result
print(f"Total DNA fragments after digestion: {fragment_total}")