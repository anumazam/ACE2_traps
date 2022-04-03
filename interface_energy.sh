for file in ../Iterative_refinement_CVD293/*
do
  ~/Rosetta/source/bin/interface_energy.macosclangrelease -in:file:s "$file" -face1 face1_293 -face2 face2_293 -score:hbond_bb_per_residue_energy -beta >>interface_energies_293
done

for file in ../Iterative_refinement_CVD432/*
do
  ~/Rosetta/source/bin/interface_energy.macosclangrelease -in:file:s "$file" -face1 face1_432 -face2 face2_432 -score:hbond_bb_per_residue_energy -beta >>interface_energies_432
done
