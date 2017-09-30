from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora,models
import gensim


# doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
# doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
# doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
# doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
# doc_e = "Health professionals say that brocolli is good for your health."

# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]




#lines = [line.rstrip('\n') for line in open('/home/amrit786/Documents/BioInfoSaha/3DCode/checkdrawsurface.m','r')]
lines = [line.rstrip('\n') for line in open('/home/amrit786/Documents/BioInfoSaha/DocIT/101repo/contributions/antlrAcceptor/org/softlang/tests/Parsing.java','r')]

#lines.sort()
#print(lines)

tok = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()
texts = []


#blocks = [[i for i in lines[2:9]],[i for i in lines[11:20]],[i for i in lines[22:35]]]

#print(blocks[0])


for i in lines:
	for j in i.split():
		if j != '':
			raw = j.lower()
			tokens = tok.tokenize(raw)

			stopped_tokens = [m for m in tokens if not m in en_stop]
			#print(stopped_tokens)
			#stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

			texts.append(stopped_tokens)
			dictionary = corpora.Dictionary(texts)

			corpus = [dictionary.doc2bow(text) for text in texts]

			ldamodel = gensim.models.ldamodel.LdaModel(corpus,num_topics = 3,id2word = dictionary,passes=20)
			print(ldamodel.print_topics(num_topics = 3, num_words = 3))

#print(texts)

# raw = doc_a.lower()

# tokens = tok.tokenize(raw)

# stopped_tokens = [i for i in tokens if not i in en_stop]

# p_stemmer = PorterStemmer()
# texts = [p_stemmer.stem(i) for i in stopped_tokens]

# dictionary = corpora.Dictionary(texts)

# corpus = [dictionary.doc2bow(text) for text in texts]

# ldamodel = gensim.models.ldamodel.LdaModel(corpus,num_topics = 3,id2word = dictionary,passes=20)
# print(ldamodel.print_topics(num_topics = 3, num_words = 3))
#print(corpus[0])
#print(dictionary.token2id)
#print(texts)
