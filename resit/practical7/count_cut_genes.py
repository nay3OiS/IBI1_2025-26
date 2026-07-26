ecori_site = "GAATTC"
input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all(1).fa"

# Get custom output filename from userp(
output_name = input("Enter output FASTA name(end with '.fa'): ")

# Create variables
current_gene = ""
seq_storage = ""
final_output = []

# Read input fasta
with open(input_fasta, "r") as f_in:
    for line in f_in:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # New gene header
        if line_clean.startswith(">"):
            # Process previous gene
            if current_gene and seq_storage:
                cut_times = seq_storage.count(ecori_site)
                fragment_num = cut_times + 1
                new_header = f">{current_gene}|Fragments:{fragment_num}"
                final_output.append(new_header)
                final_output.append(seq_storage)
            # Update gene name and reset sequence buffer
            header_split = line_clean.split()
            current_gene = header_split[0].lstrip(">")
            seq_storage = ""
        else:
            # Combine multi-line DNA sequence
            seq_storage += line_clean

# Process the last gene in file
if current_gene and seq_storage:
    cut_times = seq_storage.count(ecori_site)
    fragment_num = cut_times + 1
    new_header = f">{current_gene}|Fragments:{fragment_num}"
    final_output.append(new_header)
    final_output.append(seq_storage)

# Write filtered data to output file
with open(output_name, "w") as f_out:
    for content in final_output:
        f_out.write(content + "\n")

print(f"Done. Saved to {output_name}")