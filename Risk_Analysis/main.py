import json
import re
import pandas as pd
import requests
result = requests.get('http://api.springernature.com/meta/v2/json?q=/10.1186/s41239&s=201&p=100&api_key=fde2ad5ab663f54f74469423d417539d')

result_text = result.text

dataobj = json.loads(result_text)

list = dataobj['records']
print(len(list))
print(list[0])

# def titles():

List_titles = []
for i in range(len(list)):
    Y = list[i].get("title")
    List_titles.append(Y)
print(List_titles)

list_abstract = []
for x in range(len(list)):
    z = list[x].get("abstract")
    list_abstract.append(z)
print(list_abstract)

df2 = pd.DataFrame(list_abstract, columns=['Abstract'])
df1 = pd.DataFrame(List_titles, columns=['Title'])

Final_data = pd.concat([df1, df2], axis=1)
print(type(Final_data))
# converting to CSV file and reading the same file
Final_data.to_csv("converted.csv",encoding='utf-8')
df = pd.read_csv("converted.csv")
List_abstract = df['Abstract'].to_list()
print(List_abstract)
print(len(List_abstract))

# title preprocessing
#data_convert['Title_process'] = data_convert['Title'].map(lambda x: re.sub('[,\.!?]', '', x))

#data_convert['Title_process'] = data_convert['Title_process'].map(lambda x: x.lower())
#data_convert['Title_process'].head()


# abstract Preprocessing
#data_convert['Abstract_process'] = data_convert['Abstract'].map(lambda x: re.sub("[,\.!?]", " ", str(x)))

#data_convert['Abstract_process'] = data_convert['Abstract_process'].map(lambda x: x.lower())
#data_convert['Abstract_process'].head()

# Prepare data for LDA Analysis
import gensim
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')
list_of_simple_preprocess_data = []
for i in data_convert['Abstract_process']:
    list_of_simple_preprocess_data.append(gensim.utils.simple_preprocess(i, deacc=True, min_len=3))
texts = list_of_simple_preprocess_data

bigram = gensim.models.Phrases(list_of_simple_preprocess_data)


stops = stopwords.words('english')
stops.extend(['from', 'subject', 're', 'edu', 'use'])

import platform
print(platform.platform())
import sys
print("Python", sys.version)
import numpy
print("NumPy", numpy.__version__)
import scipy
print("SciPy", scipy.__version__)
import gensim
print("gensim", gensim.__version__)
from gensim.models import word2vec

print("FAST_VERSION", word2vec.FAST_VERSION)


def process_text(texts):
    texts = [[word for word in line if word not in stops] for line in texts]
    texts = [bigram[line] for line in texts]
    # texts = [[word for word in lemmatize(' '.join(line), allowed_tags=re.compile('(NN)'), min_length=3)] for line in texts]
    return texts


# print(process_text)

train_texts = process_text(list_of_simple_preprocess_data)

from gensim.models import LdaModel
from gensim.corpora import Dictionary

dictionary = Dictionary(train_texts)
corpus = [dictionary.doc2bow(text) for text in train_texts]

print(dictionary)
print(corpus)

ldamodel = LdaModel(corpus=corpus, num_topics=10, id2word=dictionary)
ldamodel.show_topics()

import pyLDAvis.gensim

pyLDAvis.enable_notebook()

lda_display = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary, sort_topics=False)

pyLDAvis.display(lda_display)
