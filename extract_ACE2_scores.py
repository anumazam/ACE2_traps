#!/usr/bin/python

import numpy
import pandas as pd

df_average = pd.DataFrame()
df_stdev = pd.DataFrame()

ace2_residues = []
with open ('293_ace2_res') as res_file:
    for ace2_res in res_file:
        ace2_residues.append(ace2_res.rstrip())

structure_files = []
with open ('293_files') as pdb_file:
    for structure in pdb_file:
        structure_files.append(structure.rstrip())

for residue in ace2_residues:

    summed_res_energies = [0.0] * 29
    all_energy_lists = []
    temp_energies = []
    
    for current_structure_file in structure_files:
        with open ('../Iterative_refinement_CVD293/' + current_structure_file, 'rt') as myfile:
                    
            for line in myfile:
                if residue in line:

                    for t in line.split():
                        try:
                            temp_energies.append(float(t))
                        except ValueError:
                            pass

                    if residue == 'ASN_214':
                        print(line)
                    summed_res_energies = numpy.add(temp_energies, summed_res_energies)
                    all_energy_lists.append(temp_energies)
                    temp_energies = []
    
    averaged_res_energies = numpy.mean(all_energy_lists, axis = 0)
    stdev_res_energies = numpy.std(all_energy_lists, axis = 0)
    

    df_average[residue] = averaged_res_energies
    df_stdev[residue] = stdev_res_energies
df_average.to_csv('average_432.csv', header = False, index = False, mode = 'a')
df_stdev.to_csv('stdev_432.csv', header = False, index = False, mode = 'a')

