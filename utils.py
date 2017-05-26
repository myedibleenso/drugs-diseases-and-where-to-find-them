from collections import Counter

def character_ngrams(string, n):
	ngrams = []
	string = "^" + string + "$"
	
	for i in range(0, len(string) - (n-1)):
		yield string[i:i+n]

def ngrams_from_file(file_path, nlp_pipeline, n):

	# open file, store lines as list
	with open(file_path, 'r') as f:
		lines = f.read().splitlines()
	
	# get distinct lines
	distinct_lines = set(lines)

	cnts = Counter()
	for distinct_line in distinct_lines:
		doc = nlp_pipeline.bionlp.annotate(distinct_line)
		counts_for_doc = ngrams_from_document(doc, n)
		for k,v in counts_for_doc.items():
			cnts[k] += v
	
	# normalize the dictionary
	return normalize(cnts)

def normalize(cnts_dict):
	total = sum(v for k,v in cnts_dict.items())
	return Counter({k: v / total for k,v in cnts_dict.items()})

def ngrams_from_document(doc, n):

	'''
	Takes an annotated processors.ds.Document 
	and returns its character ngrams of size n
	'''
	cnt = Counter()
	for word in doc.words:
			ngrams = character_ngrams(word, n)
			for gram in ngrams:
				cnt[gram] += 1
	return cnt