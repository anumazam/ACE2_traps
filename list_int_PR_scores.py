#!/usr/bin/python

residues = [24, 27, 28, 30, 31, 34, 35, 37, 38, 41, 42, 45, 79, 82, 83, 325, 329, 330, 353, 354, 357, 393]
not_int_res = [25, 26, 29, 32, 33, 36, 39, 40, 43, 44, 46, 80, 81, 326, 327, 328, 355, 356]
back_helix_res = [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 78]
chain = 'D'


for residue in back_helix_res:

    with open ('432_PR_default.out', 'rt') as myfile:
        current_res = ' ' + str(residue) + chain
        print(current_res)

        for line in myfile:
            if current_res in line:
                print(line[109:120])

