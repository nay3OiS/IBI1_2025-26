# define the sequence, start codon, and stop codons
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stop = ['UAA', 'UAG', 'UGA']
orf_lengths = []
# iterate through the sequence to find start codons and calculate ORF lengths
for i in range(len(seq)-2):
    codon = seq[i:i+3]
    if codon == start:
        for j in range(i+3, len(seq)-2, 3):
            stop_codon = seq[j:j+3]
            if stop_codon in stop:
                orf_length = j - i + 3
                orf_lengths.append(orf_length)
                break
# find the longest ORF length
if orf_lengths:
    longest_orf = max(orf_lengths)
    print("The length of the longest ORF is:", longest_orf)
else:
    print("No ORF found in the sequence.")
