import re
from sklearn.feature_extraction.text import TfidfVectorizer 
from nltk.tokenize import sent_tokenize

ava_stop = ['abstract', 'assert', 'boolean', 'break', 'byte' , 'byte', 'switch',
                    'case', 'try', 'catch', 'finally', 'char', 'class', 'continue', 'default',
                    'do', 'double', 'if', 'else', 'enum', 'extends', 'final', 'float', 'for', 
                    'implements', 'import' , 'instanceOf','array','int']

with open("quicksort.java", 'r') as infile:
    string = infile.read()

code = string.split('\n')
scope = ['private','public','static']
funcCondition = re.compile("private|public|static (class)!( .* ) { ")
functionList = []
for i in code:
    res = funcCondition.findall(i)
    if res:
        functionList.append(i)
finalFuncList = []
for i in functionList:
    string = i.strip()
    finalFuncList.append(string)

featureList = []

for i in finalFuncList:
    val = []
    str1 = i.lstrip("public")
    str2 = str1.lstrip("private")
    str3 = str2.lstrip("static ")
    val = str3.split(" ")
    val = val[1].split("(")
    featureList.append(val[0])   

lines = sent_tokenize(string)
print(featureList)
ngram_range = (1,1)
vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
                   lowercase=True, ngram_range=ngram_range)
mat = vect.fit_transform(featureList)
print(mat.mean())
