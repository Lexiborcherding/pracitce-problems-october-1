# input dna
dna = "AAAACCCCGGT"

# change to complimentary string
rev_dna = dna.replace("A","t").replace("T","a").replace("G","c").replace("C", "g").upper()[::-1]

print(rev_dna)
