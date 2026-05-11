# Read FASTA file
def read_fasta(filename):
    seqs = {}
    name = ''
    seq = ''
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if name:
                    seqs[name] = seq
                name = line
                seq = ''
            else:
                seq += line
        if name:
            seqs[name] = seq
    return seqs
# Check in-frame stop (ATG start)
def has_stop(seq):
    stops = ['TAA','TAG','TGA']
    found = []
    for i in range(len(seq)-2):
        if seq[i:i+3] == 'ATG':
            for j in range(i, len(seq)-2, 3):
                c = seq[j:j+3]
                if c in stops and c not in found:
                    found.append(c)
            if found:
                return True, found
    return False, []
data = read_fasta('Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
with open('stop_genes.fa','w') as out:
    for header, seq in data.items():
        gene = header.split()[0][1:]
        ok, stops = has_stop(seq)
        if ok:
            out.write(f'>{gene} {" ".join(stops)}\n{seq}\n')
print('Done! File saved: stop_genes.fa')