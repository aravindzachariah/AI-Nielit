from textblob import Word
N=raw_input("Enter the noun :")
T=Word(N)
print T.pluralize()
