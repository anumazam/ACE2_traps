#!/usr/bin/python

residue = ' 33A '

with open ('293_PR_default.out', 'rt') as myfile:
            
    for line in myfile:
        if residue in line:
            print(line)
