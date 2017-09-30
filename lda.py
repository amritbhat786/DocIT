from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora,models
import gensim
import re
#lines = [line.rstrip('\n') for line in open('/home/amrit786/Documents/BioInfoSaha/3DCode/checkdrawsurface.m','r')]
lines = [line.rstrip('\n') for line in open('/home/amrit786/Documents/BioInfoSaha/DocIT/LDA/qsort.java','r')]
lines = [line.lstrip() for line in lines]
lines = [line.rstrip(';') for line in lines]

#print(lines)
tok = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()
texts = []

cond = re.compile('\w')
lines1 = []
for i in lines:
	if cond.match(i):
		lines1.append(i)
#print(lines1)

for i in lines1:
		#print(i)
	raw = i.lower()
	tokens = tok.tokenize(raw)
		#print(tokens)
		#print(":")
		#print(type(tokens))
	stopped_tokens = [m for m in tokens if not m in en_stop]
		#print(stopped_tokens)
		#stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

	texts.append(stopped_tokens)
	dictionary = corpora.Dictionary(texts)

	corpus = [dictionary.doc2bow(text) for text in texts]
	ldamodel = gensim.models.ldamodel.LdaModel(corpus,num_topics = 2,id2word = dictionary,passes=1)
	print(ldamodel.print_topics(num_topics = 1, num_words = 3))

