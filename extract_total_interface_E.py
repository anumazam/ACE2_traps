#!/usr/bin/python

total_int_E = []
with open ('interface_energies_432', 'rt') as myfile:
    for line in myfile:
        if  "TOTAL INTERFACE ENERGY:" in line:
            if line.endswith("): 0\n") == False:
                total_int_E.append(line)

outfile = open('total_int_E_432.txt','w')
outfile.writelines(total_int_E)

myfile.close()
outfile.close()

