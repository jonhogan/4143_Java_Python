import re

sList = ['here I a, affkjaf I am ajsfhlaksfI am', 'here I am','I am here']

for s in sList:
    print(re.search('^here', s))