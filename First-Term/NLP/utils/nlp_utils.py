import re
import string

import nltk
from nltk import PorterStemmer
from nltk import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter

def download_book():
    nltk.downloader.download('book')


def count_stopwords(text):
    return len(text.split()) - len(remove_stopwords(text))


def remove_stopwords(text):
    lst = []
    stopwords_lst = stopwords.words('english')
    for token in text.split():
        if token not in stopwords_lst:
            lst.append(token)

    return " ".join(lst)


def count_punctuation(text):
    return len(text) - len(remove_punctuation(text))


def remove_punctuation(text):
    escaped_punctuation = '[' + re.escape(string.punctuation) + ']'
    return re.sub(escaped_punctuation, '', text)


def punkt_segmenter(text):
    punkt = nltk.load(r'/tokenizers/punkt/english.pickle')
    return punkt.tokenize(text)


def porter_stemmer(text):
    stem = PorterStemmer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(stem.stem(token))

    return " ".join(lst)


def lancaster_stemmer(text):
    stem = LancasterStemmer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(stem.stem(token))

    return " ".join(lst)


def word_net_lemmatizer(text):
    lem = WordNetLemmatizer()
    lst = []
    for token in nltk.word_tokenize(text):
        lst.append(lem.lemmatize(token))

    return " ".join(lst)

def create_gram(text, n):
    txt = " ".join(text)
    tokens = txt.split()
    gram = [" ".join(tokens[i:i+n]) for i in range (len(tokens)-n+1)]
    print("\n Result_Create Gram \n")
    print(gram)
    return gram

def counter_gram(text,n):
    tokens =create_gram(text, n)
    print("\n Result_Count Grams \n")
    print(Counter(tokens))
   
    
    



