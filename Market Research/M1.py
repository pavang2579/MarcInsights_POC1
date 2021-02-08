from urllib.request import urlopen
import heapq
import bs4 as bs
import urllib.request
import re
import pandas as pd
import ssl
import nltk
ssl._create_default_https_context = ssl._create_unverified_context
scraped_data = urllib.request.urlopen('https://www.grandviewresearch.com/industry-analysis/education-technology-market?utm_source=prnewswire&utm_medium=referral&utm_campaign=ict_20-july-20&utm_term=education-technology-market&utm_content=rd1')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sentence_list = nltk.sent_tokenize(article_text)
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                      sentence_scores[sent] = word_frequencies[word]
                else:
                      sentence_scores[sent] += word_frequencies[word]
                      sentence_scores
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print(summary)
text_file = open("report_grandviewreview.txt", "wt")
n = text_file.write(summary)
text_file.close()
table = parsed_article.find('div', {'class': 'report_summary full'})
new_table = []
for row in table.find_all('tr')[1:]:
    column_marker = 0
    columns = row.find_all('td')
    new_table.append([column.get_text() for column in columns])
df = pd.DataFrame(new_table, columns=['Report Attribute', 'Details'])
df['Report Attribute'] = df['Report Attribute'].str.replace('\n', '')
df['Details'] = df['Details'].str.replace('\n', '')
print(df)
df.to_csv("report_grandviewreview.csv",index_label=False)