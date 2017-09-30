from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import re

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

java_stop = ['abstract', 'assert', 'boolean', 'break', 'byte' , 'byte', 'switch',
                    'case', 'try', 'catch', 'finally', 'char', 'class', 'continue', 'default',
                    'do', 'double', 'if', 'else', 'enum', 'extends', 'final', 'float', 'for', 
                    'implements', 'import' , 'instanceOf','array','int']

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 

with open("quicksort.java" ,'r' ) as infile:
    string = infile.read()

code = string.split('\n')
condition = re.compile("\/\/")
commList = []

for i in code:
    res = condition.findall(i)
    if res:
        commList.append(i)

# compile sample documents into a list


# list for tokenized documents in loop

# loop through document list
for i in code:
    texts = []
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in java_stop]
    stopped_tokens = [i for i in stopped_tokens if i not in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    # print(corpus)

# generate LDA model
    try:
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
        print(ldamodel.print_topics(num_topics=2, num_words=6))
    except ValueError:
        pass