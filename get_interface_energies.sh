for file in 313_models/*
do
  ~/Rosetta/main/source/bin/interface_energy.macosclangrelease -in:file:s "$file" -face1 face1_293 -face2 face2_293 -score:hbond_bb_per_residue_energy -beta -corrections::beta_nov16 >>interface_energies_313models
done
