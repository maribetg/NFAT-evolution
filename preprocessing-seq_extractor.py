#!/usr/bin/python

#Import the packages
from Bio import SeqIO
import sys
import string

#Data
fasta = open('protein-NFAT.fasta')
output = open('NFAT1.fasta', 'w')

#Sequence extraction from the original file
seq = ''
for line in fasta:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':
        if '1' in header:
            output.write(header + seq)
        header = line
        seq = ''


if "1" in header[-1]:
    output.write(header + seq)


output.close()
