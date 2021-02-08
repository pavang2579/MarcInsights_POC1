import bs4 as bs
import urllib.request
import re
import ssl
import nltk
import heapq
ssl._create_default_https_context = ssl._create_unverified_context
scraped_data = urllib.request.urlopen('https://uk.rs-online.com/web/generalDisplay.html?id=did-you-know/the-edtech-report')
article = scraped_data.read()
parsed_article = bs.BeautifulSoup(article,"lxml")
paragraphs = parsed_article.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sentence_list = nltk.sent_tokenize(article_text)
#nltk.download('stopwords')
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
text_file = open("report_rsonline.txt", "wt")
n = text_file.write(summary)
text_file.close()
imgs = parsed_article.find_all('img', {'src':re.compile('.jpg')})
img_urls = []
for img in imgs:
    url = img['src']
    img_urls.append(url)
print(img_urls)
import pandas as pd
df = pd.DataFrame(img_urls,columns=["image_urls"])
df.to_csv("report_imageurls_rsonline.csv")
from PIL import Image
import requests
im = Image.open(requests.get(img_urls[10], stream=True).raw)
im.show()