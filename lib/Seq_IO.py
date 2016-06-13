# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:57:35 2015

Please feel free to contact with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""


def check_ambiguous(seq, length):
    if seq.count('N') > length:
        return True
    else:
        return False
    

def check_homop(seq, length):
    seq_homop = [i*length for i in ['A','T','C','G']]
    for i in seq_homop:
        if i in seq:
            return True
    return False
    

def count_bases(seq):
    bases_number = {'A':0,'T':0,'C':0,'G':0}
    for base in bases_number:
        bases_number[base] = seq.count(base)
    return bases_number

        
def count_ambiguous(seq):
    return seq.count('N')


def count_homop(seq):
    count_homop = {'All':0,'A':0,'T':0,'C':0,'G':0}
    base_list = [i for i in count_homop]
    seq_length = len(seq)
    for base in base_list:
        for i in range(seq_length):
            homop = base*(i+1) # Generate a homopolymer with certain length
            if homop in seq:
                count_homop[base] = i+1
            else:
            # Do not found homopolyer at the given length, break the loop
                break
    max_length = max([count_homop[i] for i in count_homop])
    count_homop['All'] = max_length
    return count_homop


def pick_seqs(fasta,name_list):
    # Pick sequences based on the name list input:
    # This method is slow compared to using a dictionary
    fasta_picked = []
    for record in fasta:
        if record[0] in name_list:
            fasta_picked.append(record)
            del name_list[name_list.index(record[0])]
        if name_list == []:
            break
    return fasta_picked


def make_dict(seqs):
    # Convert a seqs list into dictionary using sequence name as keys
    seqs_dict = {}
    for record in seqs:
        seqs_dict[record[0]] = record[1:]
    return seqs_dict
    
def nucl_freq(input_seq, tail=False):
    pass