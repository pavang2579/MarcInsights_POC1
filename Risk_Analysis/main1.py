import pandas as pd
import re
df = pd.read_csv("converted.csv")

List_abstract = df['Abstract'].to_list()
print(List_abstract)
print(len(List_abstract))

List_title = df['Title'].to_list()
print(List_title)
print(len(List_title))

List1 = []
for i in List_abstract:
    r = re.sub('[,.!?]','', str(i))
    r1 = r.lower()
    List1.append(r1)
    print(List1)

import gensim
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()
#nltk.download('stopwords')
from nltk.corpus import stopwords

list_of_simple_preprocess_data = []
for i in List1:
    list_of_simple_preprocess_data.append(gensim.utils.simple_preprocess(i, deacc=True, min_len=5))
texts = list_of_simple_preprocess_data

bigram = gensim.models.Phrases(list_of_simple_preprocess_data)

stops = stopwords.words('english')

def process_text(texts):
    texts = [[word for word in line if word not in stops] for line in texts]
    texts = [bigram[line] for line in texts]
    return texts

train_texts = process_text(list_of_simple_preprocess_data)
print(train_texts)

from gensim.models import LdaModel
from gensim.corpora import Dictionary

dictionary = Dictionary(train_texts)
corpus = [dictionary.doc2bow(text) for text in train_texts]

ldamodel = LdaModel(corpus=corpus, num_topics=10, id2word=dictionary)
ldamodel.show_topics()

import pyLDAvis.gensim
import pickle
import pyLDAvis
import os

LDAvis_data_filepath = os.path.join(str(10))

# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)

# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)

pyLDAvis.save_html(LDAvis_prepared,str(10) +'.html')



