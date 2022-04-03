#!/usr/bin/python

pairwise_shortrange = []
with open ('interface_energies_432', 'rt') as myfile:
    for line in myfile:
        if  " --- " in line:
            if line.endswith("): 0\n") == False:
                pairwise_shortrange.append(line)

outfile = open('pairwise_shortrange_432.txt','w')
outfile.writelines(pairwise_shortrange)

myfile.close()
outfile.close()
