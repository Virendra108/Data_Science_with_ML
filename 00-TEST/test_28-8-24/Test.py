# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:06:29 2024

@author: viren
"""
"""1. Implement a simple Named Entity Recognition (NER)
function that identifies named entities in a sentence. The
function should return a list of these named entities.
For example, given the sentence "Ramesh lives in
Mumbai", the function should return ["Ramesh",
"Mumbai"].
Text1: “James is the author of Atomic Habits”
Text2: “Aarti works at Accenture”
"""







"""2.Design a function that classifies a text as either "spam"
or "imp" (non-spam) based on the presence of certain
keywords. For example, if the text contains words like
"buy", "free", "offer", or "click", it should be classified as
"spam". If these words are not present, the text should be
classified as "imp". The function should return the
appropriate classification.
Text1: “Buy 1 Get 1 Free”
Text2: “Meeting is scheduled at 12 PM ”
Text2: “Click on the link below to see the offer.”
"""














"""3. Create a function that should return a list of stemmed
words.
e.g [‘running’] = [‘run’]
list = [‘painful’,’standing’,’abstraction’,’magically’]
"""
import nltk
stemmer=nltk.stem.PorterStemmer()
lst1=['painful','standing','abstraction','magically']
lst2=[]
for word in lst1:
    lst2.append(stemmer.stem(word))
print(lst2)






"""4. Implement a function that takes a list of tokens (words)
and removes all stopwords from it. For example, if the
input tokens are ["This", "is", "a", "test"] and
the stopwords are ["is", "a", "the"], the function should
return ["This", "test"].
Stopwords = [“is”,”a”,”the”, “an”,”she”]
Sentence1: “an apple is on the table.”
Sentence2: “She is an engineer.”
"""









"""5 . Perform lemmatzation on the given text
 text= "Dancing is an art. Students should be taught
dance as a subject in schools . I danced in many of my
school function. Some people are always hesitating
to dance."
"""
"""
from nltk import WordNetLemmatizer
text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."
token=text.split()
lemma=WordNetLemmatizer()
final=lemma.lemmatize(token)
"""


import spacy
nlp=spacy.load('en_core_web_sm')
text1=nlp(u"Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance.")
for token in text1:
    print(token.lemma_)


