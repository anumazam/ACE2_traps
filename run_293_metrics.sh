for file in ../Iterative_refinement_CVD293/*
do
  ~/Rosetta/main/source/bin/rosetta_scripts.macosclangrelease -database ~/Rosetta/main/database -in:file:s "$file" -parser:protocol metrics.xml  -out:file:score_only score -beta -corrections::beta_nov16 >>metrics_293
done
