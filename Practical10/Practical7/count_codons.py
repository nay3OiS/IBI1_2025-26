import matplotlib.pyplot as plt
plt.switch_backend('Agg')
# Read FASTA
def read_fasta(file):
    seqs = []
    s = ''
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if s:
                    seqs.append(s)
                s = ''
            else:
                s += line
        if s:
            seqs.append(s)
    return seqs
# Get codons before target stop
def get_codons(seq, target):
    codons = []
    for i in range(len(seq)-2):
        if seq[i:i+3] == 'ATG':
            temp = []
            for j in range(i, len(seq)-2, 3):
                c = seq[j:j+3]
                if c == target:
                    codons = temp
                    break
                temp.append(c)
    return codons
# Input stop codon
target_stop = input("Enter stop codon (TAA/TAG/TGA): ").upper()
# Read all sequences
all_seqs = read_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# Collect all codons
all_codons = []
for s in all_seqs:
    all_codons += get_codons(s, target_stop)
# Count codons WITHOUT collections
count_dict = {}
for codon in all_codons:
    if codon in count_dict:
        count_dict[codon] += 1
    else:
        count_dict[codon] = 1
# Print result
print("Codon counts:")
for c, n in count_dict.items():
    print(c, n)
# Draw and save pie chart
plt.pie(count_dict.values(), labels=count_dict.keys(), autopct='%1.1f%%')
plt.title(f'Codon distribution for {target_stop}')
plt.savefig(f'pie_{target_stop}.png')
print(f"Pie chart saved as pie_{target_stop}.png")