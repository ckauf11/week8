#!/usr/bin/env python

# prompt- do you want to translate or pull a codon
print (30 * "-" , "MENU" , 30 * "-")
print("1.translate a protein-coding nucleotide sequence to amino acids")
print("2. randomly draw a codon from the sequence")
print (67 * "-")

choice = input("Enter your choice")
#if-else to do option 1
if choice == "1":
	dnaSeq = input("Enter DNA sequence in all caps:")
#DNA --> RNA
	rnaSeq=dnaSeq.replace("T","U")
	print("transcribed RNA sequence: ")
	print(rnaSeq)

#dictionary to translate amino acids and codons
	codon={"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}
# rna to amino acids
dnaSeq = input("Enter DNA sequence in all caps:")
rnaSeq = dnaSeq.replace("T","U")
proteinSeq = ""
codon ={}
for n in range(0, len(rnaSeq), 3):
	if rnaSeq[n:n+3] in codon:
		proteinSeq = codon[rnaSeq[n:n+3]]
	print ("Protein Sequence: ")
	print ("proteinSeq")


#if else for option 2 
#input dna or split dna into a list 
else:
        dnaSeq = input("Enter DNA sequence in all caps")
        codon2 = [dnaSeq[i:i+3] for i in range(0, len(dnaSeq), 3)]
        print(codon2)

#print random codon
import random 
randomCodon= random.choice(codon2)
print(randomCodon)
