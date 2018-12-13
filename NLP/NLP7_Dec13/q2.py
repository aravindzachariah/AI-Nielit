"""
	Create a few sentences . Find the frequency count of the words in the vocabulary.
	2. Cluster the words in the sentences  based on the count.
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
"Browsers help us to search for information",
"Games refresh our minds",
"Chrome is a Browser",
"Football is an interesting Game",
"Cricket is also an interesting Game",
"You can open many tabs in Browsers"]

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(documents)
dict = tfidf.vocabulary_
print tfidf.vocabulary_
counts = dict.values()

length = len(dict.keys())
x_lab = []
for key in dict.keys():
	x_lab.append(key)

print 'Length :', length
words = np.arange(0,length)

model = KMeans(n_clusters=length);
X = list(zip(words, counts))
model.fit(X)

print(model.labels_)
print dict.keys()

plt.scatter(words,counts,c=model.labels_)
plt.xlabel("Words")
plt.ylabel("Occurance")
plt.xticks(words, x_lab, rotation=90)
#plt.legend(loc="best", labels=x_lab)
plt.show()
