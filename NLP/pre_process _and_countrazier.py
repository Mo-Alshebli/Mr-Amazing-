import pandas as pd
import string
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer

class pre_proccess_nlp:

    def __init__(self):
        # Initialize the WordNet Lemmatizer, Porter Stemmer, and stopwords
        self.lim = nltk.WordNetLemmatizer()
        self.str = nltk.PorterStemmer()
        self.stopWord = nltk.corpus.stopwords.words('english')

    def preproccess(self, text):
        # Perform pre-processing steps on the text
        text = self.Remove_punctuation(text)
        text = self.Tokenization(text)
        text = self.remove_stopwords(text)
        text = self.steming(text)
        text = self.lematizing(text)
        return text

    def CountVectorizer_(self, data):
        # Initialize the CountVectorizer with the pre-processing function
        count_vec = CountVectorizer(analyzer=self.preproccess)
        # Fit and transform the data using CountVectorizer
        X_count = count_vec.fit_transform(data)
        # Convert the transformed data to a DataFrame
        dataset = pd.DataFrame(X_count.toarray())
        return dataset

    def Remove_punctuation(self, text):
        # Remove punctuation from the text
        text_nopun = "".join([char for char in text if char not in string.punctuation])
        return text_nopun

    def Tokenization(self, text):
        # Tokenize the text using regular expression
        toknes = re.split('\W+', text)
        return toknes

    def remove_stopwords(self, text):
        # Remove stopwords from the text
        text_stop = [word for word in text if word not in self.stopWord]
        return text_stop

    def stemming(self, text):
        # Perform stemming on the text
        text = [self.str.stem(word) for word in text]
        return text

    def lematizing(self, stemword):
        # Perform lemmatization on the text
        text = [self.lim.lemmatize(word) for word in stemword]
        return text
