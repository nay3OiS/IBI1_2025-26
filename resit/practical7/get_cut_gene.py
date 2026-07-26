ecori_motif = "GAATTC"
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all(1).fa"
output_fasta = "cut_genes.fa"

# store current gene info
gene_name = ""
seq_buffer = ""
output_records = []

with open(input_fasta, "r") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        
        # new gene header line
        if line.startswith(">"):
            # process previous gene if exists
            if gene_name and seq_buffer:
                if ecori_motif in seq_buffer:
                    seq_len = len(seq_buffer)
                    new_header = f">{gene_name}|Length:{seq_len}"
                    output_records.append(new_header)
                    output_records.append(seq_buffer)
            # extract gene name from header
            header_parts = line.split()
            gene_name = header_parts[0].lstrip(">")
            seq_buffer = ""
        else:
            # append DNA sequence, combine multi-line
            seq_buffer += line
    
    # handle the last gene after loop ends
    if gene_name and seq_buffer:
        if ecori_motif in seq_buffer:
            seq_len = len(seq_buffer)
            new_header = f">{gene_name}|Length:{seq_len}"
            output_records.append(new_header)
            output_records.append(seq_buffer)

# write filtered result to output file
with open(output_fasta, "w") as outfile:
    for entry in output_records:
        outfile.write(entry + "\n")

print(f"Filter complete. Results saved to {output_fasta}")