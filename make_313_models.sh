for file in ../../20211127/Iterative_refinement_CVD293_no901/*
do
  ~/Rosetta/main/source/bin/rosetta_scripts.macosclangrelease -database ~/Rosetta/main/database -in:file:s "$file" -parser:protocol make_313_muts.xml -beta_nov16 -corrections::beta_nov16 >>make_313_models.log
done
