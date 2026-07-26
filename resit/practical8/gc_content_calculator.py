def calculate_gc(dna_seq):
    # Convert all sequence to uppercase
    seq_upper = dna_seq.upper()
    valid_bases = {"A", "T", "C", "G"}
    # Check every character in sequence
    for base in seq_upper:
        if base not in valid_bases:
            raise ValueError("Sequence contains invalid DNA characters")
    # Count G and C bases
    g_count = seq_upper.count("G")
    c_count = seq_upper.count("C")
    total_length = len(seq_upper)
    gc_percent = (g_count + c_count) / total_length * 100
    return gc_percent

# Example call
if __name__ == "__main__":
    seq_test = "ATGCGGATTC"
    gc_result = calculate_gc(seq_test)
    print(f"GC content: {gc_result:.2f} %")