def extract_gene_name(header):
    """Extract yeast gene name (starts with uppercase Y) using only string operations"""
    gene_name = ""
    start_index = -1
    # Find the first uppercase Y (standard yeast gene name start)
    for i in range(len(header)):
        if header[i] == 'Y':
            start_index = i
            break
    if start_index == -1:
        return "unknown_gene"
    # Collect consecutive letters/numbers after Y to form gene name
    for char in header[start_index:]:
        if 0<=char<=9 or 'a'<=char<='z' or 'A'<=char<='Z':
            gene_name += char
        else:
            break
    return gene_name if gene_name else "unknown_gene"

def has_in_frame_stop(sequence):
    """Find in-frame stop codons (TAA/TAG/TGA) that start with ATG"""
    stop_codons = {"TAA", "TAG", "TGA"}
    found_stops = set()
    seq_length = len(sequence)

    # Check all possible ATG start positions
    for start in range(seq_length - 2):
        if sequence[start:start+3] == "ATG":
            # Check every 3 nucleotides after ATG for stop codons
            for i in range(start + 3, seq_length - 2, 3):
                current_codon = sequence[i:i+3]
                if current_codon in stop_codons:
                    found_stops.add(current_codon)
            # Exit early if stop codons are found
            if found_stops:
                break
    return found_stops

def process_fasta(input_file, output_file):
    """Read FASTA file, filter genes with in-frame stop codons, write new FASTA"""
    # Check if input file exists
    import os
    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found - {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as file_in, \
         open(output_file, 'w', encoding='utf-8') as file_out:

        current_header = ""
        current_sequence = ""

        for line in file_in:
            line = line.strip()
            if not line:
                continue

            # New FASTA entry starts with >
            if line.startswith(">"):
                # Process the previous complete sequence
                if current_header and current_sequence:
                    gene_name = extract_gene_name(current_header)
                    stop_set = has_in_frame_stop(current_sequence)
                    # Only keep genes with at least one in-frame stop codon
                    if stop_set:
                        stop_string = "|".join(sorted(stop_set))
                        new_header = f">{gene_name} {stop_string}"
                        file_out.write(f"{new_header}\n{current_sequence}\n")
                # Reset for new sequence
                current_header = line
                current_sequence = ""
            else:
                # Concatenate multi-line sequence
                current_sequence += line

        # Process the last sequence in the file
        if current_header and current_sequence:
            gene_name = extract_gene_name(current_header)
            stop_set = has_in_frame_stop(current_sequence)
            if stop_set:
                stop_string = "|".join(sorted(stop_set))
                new_header = f">{gene_name} {stop_string}"
                file_out.write(f"{new_header}\n{current_sequence}\n")
    print(f"SUCCESS: Process completed. Results saved to {output_file}")

if __name__ == "__main__":
    # --------------------------
    # Set your file path here
    # Use absolute path to avoid FileNotFoundError
    # --------------------------
    INPUT_FASTA = r"C:\Users\11467\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    OUTPUT_FASTA = "stop_genes.fa"
    
    process_fasta(INPUT_FASTA, OUTPUT_FASTA)