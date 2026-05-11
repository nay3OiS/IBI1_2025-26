seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stops = ['UAA', 'UAG', 'UGA']
longest_len = 0
longest_orf = ''
# Find all AUG start positions
for i in range(len(seq) - 2):
    if seq[i:i+3] == start:
        # Search in frame
        for j in range(i, len(seq)-2, 3):
            codon = seq[j:j+3]
            if codon in stops:
                current_orf = seq[i:j]
                current_len = len(current_orf)
                if current_len > longest_len:
                    longest_len = current_len
                    longest_orf = current_orf
                break
print("Longest ORF:", longest_orf)
print("Length:", longest_len)