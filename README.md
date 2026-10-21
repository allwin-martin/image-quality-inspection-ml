# Image Quality Inspection — Rule-Based Baseline

Simple brightness and contrast quality checks for ASCII PGM (P2) images. **This is not yet a trained machine-learning classifier.**

## Run
```bash
python quality_check.py sample.pgm
python -m unittest discover -p "test_*.py"
```

## Demo
Edit a copy of the sample to make it darker, brighter or uniformly grey; compare resulting flags. Discuss threshold sensitivity and why global statistics miss local defects.

## Next phase
Build a labelled image dataset, extract features, train and evaluate an ML classifier, and report actual held-out metrics. No model accuracy is claimed.
