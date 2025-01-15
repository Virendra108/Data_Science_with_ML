# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:08:54 2024

@author: viren
"""

'''Q1  Write a NLTK program to omit some given stop words
from the stopwords list.
Stopwords to omit : 'again', 'once', 'from'
'''
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
Stop_words=set(stopwords.words('english'))

#Stopwords to omit : 'again', 'once', 'from'
lists=['again', 'once', 'from']
for element in lists:
    Stop_words.remove(element)
print(Stop_words)

'''2. Build a Named Entity Recognition (NER) model that identifies
entities (people, locations, organizations) in text using
advanced models like LSTM-CRF or BERT. Compare the
performance of these models.
Note : Use the ‘conll2003’ dataset from dataset library for this problem
'''











'''3. Create a text summarization model using BART to generate
summaries from news articles.
Note : Use cnn_dailymail dataset
'''











'''4. Implement basic text preprocessing steps on a dataset,
including tokenization, lowercasing, removing stopwords,
punctuation, and special characters.
text = "Hello! This is a sample text. Let's tokenize it, remove stopwords and
punctuations. Hope you all are doing well!"
'''
text = "Hello! This is a sample text. Let's tokenize it, remove stopwords and punctuations. Hope you all are doing well!"
text=text.lower()
tokenz=[text.split()]
Stop_to_remove=set(stopwords.words('english'))
for word in Stop_to_remove:
    for token in tokenz:
        if(word==token):
            tokenz.remove()

'''5. Perform basic sentiment analysis on text using a Bag-ofWords model. Build a classifier to predict whether a review is
positive or negative.
Dataset : books.csv'''
import pandas as pd
df=pd.read_csv('D:/data science/test_27-9-24/books.csv')


