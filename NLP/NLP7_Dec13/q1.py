"""
	1. Create a few sentences . Find the frequency count of the words in the vocabulary.
"""

from sklearn.cluster import KMeans;
import matplotlib.pyplot as py;
from sklearn.feature_extraction.text import TfidfVectorizer;

documents = [
"Browsers help us to search for information",
"Games refresh our minds",
"Chrome is a Browser",
"Football is an interesting Game",
"Cricket is also an interesting Game",
"You can open many tabs in Browsers"];

tfidf = TfidfVectorizer(stop_words='english');
tfidf.fit(documents);

print tfidf.vocabulary_