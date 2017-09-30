
with open("bsort.java", 'r') as infile:
    string = infile.read()

lineCount = 0
code = string.split('\n')
for i in code:
    lineCount += 1
print(lineCount)
