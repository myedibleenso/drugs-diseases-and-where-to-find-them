# Todo

## Generated rules using corpus statistics

1. Calculate the relative frequency of character n-grams on our annotated abstracts (`processors.ds.Document`).
2. `diff` that with the distribution for drug names
3. Auto-generate rules for Named Entity Recognition (NER)

## Detecting `HasAdverseOutcome` relations
	- components of relation:
		- `biomarker: BioMarker`
		- `treatment: Treatment`
		- `disease: Disease`
	- attach cell line context

## Sensitivity Vs. Resistance Classifier