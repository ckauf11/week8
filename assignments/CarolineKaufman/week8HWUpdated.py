#!/usr/bin/env  python

#Presents menu options for user to choose from.
print ("Choose from the menu below: ")
menu = input("1. Translate a protein-coding nucleotide sequence to amino acids:  \n -or- 2. Randomly draw a codon from the sequence: ")

#If 1: enter DNA Sequence
if menu == "1":
	dnaSeq = input("Please enter DNA Sequence in all CAPS: ")

#Converts the DNA sequence --> RNA sequence. 
	rnaSeq = dnaSeq.replace("T","U")
	print("DNA sequence to RNA sequence: "+rnaSeq)

#Made a codon to amino acid dictionary.
	Codon2AA = {"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn",
               	    "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
                    "AGA":"Arg", "AGC":"Ser", "AGG":"Arg", "AGU":"Ser",
                    "AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
		    "CAA":"Gln", "CAC":"His", "CAG":"Gln", "CAU":"His",
                    "CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro",
                    "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
                    "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",
		    "GAA":"Glu", "GAC":"Asp", "GAG":"Glu", "GAU":"Asp",
                    "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
                    "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
                    "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
		    "UAA":"_",   "UAC":"Tyr", "UAG":"_",   "UAU":"Thr",
                    "UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
                    "UGA":"_",   "UGC":"Cys", "UGG":"Trp", "UGU":"Cys",
                    "UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

#Converts the RNA sequence -->  amino acids. 
	proteinSeq = ""
	for i in range(0, len(rnaSeq), 3):	# DB: An additional comment or two here might be helpful
		if rnaSeq[i:i+3] in Codon2AA:
			proteinSeq += Codon2AA[rnaSeq[i:i+3]]
	print ("Protein Sequence: "+proteinSeq)

#This is if the user enters number 2.
#Enter their DNA sequence; sequence is then split into a list of codons.
else:
	dnaSeq = input ("Please enter DNA Sequence in all CAPS: ")
	codon = [dnaSeq[n:n+3] for n in range(0, len(dnaSeq), 3)]
	print(codon)

#One random codon chosen from DNA sequence entered
	import random	# DB: Better to put this at the top of the script.
	randomCodon = random.choice(codon)
	print(randomCodon)

# DB: Overall, very good! Just a couple minor comments (see above).
