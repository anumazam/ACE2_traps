#!/usr/bin/python
import numpy as np

all_interactions = []
with open ('pairwise_shortrange_293.txt', 'rt') as infile:
    for line in infile:
        label = line.split(':')
        all_interactions.append(label[0])
infile.close()

unique_interactions = []
for element in all_interactions:
    if element not in unique_interactions:
        unique_interactions.append(element)

interactions_dict = dict.fromkeys(unique_interactions, [])

with open ('pairwise_shortrange_293.txt', 'rt') as infile:
    for line in infile:
        line = line.strip()
        label = line.split(':')
        interaction_val = float(label[1])
        temp_key = label[0]
        interactions_dict[temp_key] = [interactions_dict[temp_key],interaction_val]

infile.close()

for key, value in interactions_dict.items():
    flat_value = str(value)
    flat_value = flat_value.replace("[", "")
    flat_value = flat_value.replace("]", "")
    temp_list = []
    flat_values = flat_value.split(",")
    for item in flat_values:
        if len(item) > 0:
            temp_list.append(float(item))
    interactions_dict[key] = temp_list

averaged_interactions_dict = dict.fromkeys(unique_interactions, [])
stdev_interactions_dict = dict.fromkeys(unique_interactions, [])
for key, value in interactions_dict.items():
    avg_value = np.mean(value)
    stdev_value = np.std(value)
    averaged_interactions_dict[key] = avg_value
    stdev_interactions_dict[key] = stdev_value
    
outfile = open('pairwise_avg_293.csv','w')
for key in averaged_interactions_dict.keys():
    outfile.write("%s,%s,%s\n"%(key, averaged_interactions_dict[key], stdev_interactions_dict[key]))
outfile.close()
