import matplotlib.pyplot as plt

def extract_gene_name(header):
    """Extract gene name starting with Y"""
    gene_name = ""
    start_idx = -1
    for i in range(len(header)):
        if header[i] == 'Y':
            start_idx = i
            break
    if start_idx == -1:
        return "unknown_gene"
    for c in header[start_idx:]:
        if 0<=c<=9 or 'a'<=c<='z' or 'A'<=c<='Z':
            gene_name += c
        else:
            break
    return gene_name

def get_longest_orf_upstream(seq, target_stop):
    """Get upstream codons of the longest ORF ending with target_stop"""
    start_codon = "ATG"
    seq_length = len(seq)
    longest_upstream = ""

    for i in range(seq_length - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i + 3, seq_length - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    upstream = seq[i:j]
                    if len(upstream) > len(longest_upstream):
                        longest_upstream = upstream
                    break
    return longest_upstream

def count_codons(upstream_seq):
    """Count all in-frame codons"""
    codon_counts = {}
    for i in range(0, len(upstream_seq) - 2, 3):
        codon = upstream_seq[i:i+3]
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1
    return codon_counts

def count_all_genes(input_file, target_stop):
    """Read FASTA and count codons for target stop codon"""
    total_counts = {}
    current_header = ""
    current_seq = ""

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header and current_seq:
                    upstream = get_longest_orf_upstream(current_seq, target_stop)
                    if upstream:
                        codons = count_codons(upstream)
                        for c, n in codons.items():
                            total_counts[c] = total_counts.get(c, 0) + n
                current_header = line
                current_seq = ""
            else:
                current_seq += line

    # Process last sequence
    if current_header and current_seq:
        upstream = get_longest_orf_upstream(current_seq, target_stop)
        if upstream:
            codons = count_codons(upstream)
            for c, n in codons.items():
                total_counts[c] = total_counts.get(c, 0) + n
    return total_counts

def create_pie_chart(counts, stop_codon):
    """Create and save pie chart to file"""
    if not counts:
        print("No codon data to plot")
        return

    labels = list(counts.keys())
    sizes = list(counts.values())

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Codon Distribution Upstream of {stop_codon}")
    plt.savefig(f"codon_pie_{stop_codon}.png", dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Pie chart saved as codon_pie_{stop_codon}.png")

if __name__ == "__main__":
    FASTA_FILE = r"C:\Users\11467\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

    # Get valid stop codon input
    valid = ["TAA", "TAG", "TGA"]
    user_input = ""
    while user_input not in valid:
        user_input = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()

    print(f"Counting codons for {user_input}...")
    counts = count_all_genes(FASTA_FILE, user_input)
    print("Codon counts:", counts)
    create_pie_chart(counts, user_input)