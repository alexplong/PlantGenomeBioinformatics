#!/usr/bin/python

from Bio import SeqIO


record = SeqIO.read('AT1G04020.gb', 'genbank')

#print len(record)
#print record.id
#print record.seq
print(record.features[2])
