
#save a nucleotide sequence as a variable
seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" 

#save variables with starting zero count
a_count = 0
g_count = 0 
c_count = 0
t_count = 0

#loop through the sequence counting each AGCT
for nuc in seq:
    if nuc == "A":
        a_count += 1
    elif nuc == "G":
        g_count += 1
    elif nuc == "C":
        c_count += 1 
    elif nuc == "T":
        t_count += 1

# print out the number of each  nucleotide present ACGT\
print(a_count, g_count, c_count, t_count)

# Try .count
print(seq.count("A"), seq.count("G"), seq.count("C"), seq.count("T"))
