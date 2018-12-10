#!/usr/bin/env python

dnaSeq = input ("Type DNA Sequence: ")

#complement dna 

dnaSeq = dnaSeq.lower()
dnaSeq = dnaSeq.replace("c","G")
dnaSeq = dnaSeq.replace("g","C")
dnaSeq = dnaSeq.replace("t","A")
dnaSeq = dnaSeq.replace("a","T")

#reverse sequence
print(dnaSeq[::-1])

# DB: Good! This is the script you sent to me by email. Simple, clean, works.
