from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import re

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

java_stop = [
             'abstract', 'assert', 'boolean', 'break', 'byte', 'switch',
             'case', 'try', 'catch', 'finally', 'char', 'class', 'continue',
             'default', 'do', 'double', 'if', 'else', 'enum', 'extends',
             'final', 'float', 'for', 'implements', 'import', 'instanceOf',
             'array', 'int'
             ]

# Create p_stemmer of class PorterStemmer
# p_stemmer = PorterStemmer()

with open("qsort.java", 'r') as infile:
    string = infile.read()

code = string.split('\n')
condition = re.compile("\/\/")
commList = []
wordList = []

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
    stopped_tokens = [i for i in tokens if i not in java_stop]
    stopped_tokens = [i for i in stopped_tokens if i not in en_stop]

    # stem tokens
    # stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    # add tokens to list
    texts.append(tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]
    # print(corpus)

    # generate LDA model
    try:
        ldamodel = gensim.models.ldamodel.LdaModel(
                                                   corpus, num_topics=2,
                                                   id2word=dictionary,
                                                   passes=20)
        topiclist = ldamodel.show_topics(
                                         num_topics=1, num_words=6, log=True,
                                         formatted=True

                                         )
        tl = []
        for i in topiclist:
            tl.append(i)
            for j in tl:
                element = j[1]
                wordList.append(re.compile('[a-zA-Z]+').findall(element))
    except ValueError:
        pass

justWords = []
for i in wordList:
    for j in i:
        justWords.append(j)

dictionary = corpora.Dictionary(wordList)
print(wordList)
corpus = [dictionary.doc2bow(text) for text in wordList]
ldamodel = gensim.models.ldamodel.LdaModel(
                                           corpus, num_topics=2,
                                           id2word=dictionary, passes=5
                                          )
print(ldamodel.show_topics(
                           num_topics=1, num_words=10, log=True,
                           formatted=True
                          ))
