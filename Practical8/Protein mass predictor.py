def protein_mass(sequence):
    # Amino acid masses in atomic mass units (amu)
    aa_mass = {'G': 57.02,'A': 71.04,'S': 87.03,'P': 97.05,'V': 99.07,'T': 101.05,'C': 103.01,'I': 113.08,'L': 113.08,'N': 114.04,'D': 115.03,'Q': 128.06,'K': 128.09,'E': 129.04,'M': 131.04,'H': 137.06,'F': 147.07,'R': 156.10,'Y': 163.06, 'W': 186.08}
    total_mass = 0.0
    for aa in sequence():
        if aa not in aa_mass:
            print("Error: Invalid amino acid:",aa)
        total_mass += aa_mass[aa]
    return total_mass
# Examples
seq1 = "GASPV"
mass1 = protein_mass(seq1)
print("Sequence:",seq1,"Mass:",mass1)
seq2 = "AXYZ"  # Will trigger an error due to invalid amino acids
mass2 = protein_mass(seq2)
print("Sequence:",seq2,"Mass:",mass2)