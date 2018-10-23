### DICIONÁRIO / BOW #####

import nltk
import string
import csv
from gensim import corpora
from nltk.tokenize import TweetTokenizer
import numpy as np

stemmer = nltk.stem.RSLPStemmer()
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
translator = str.maketrans('', '', string.punctuation)
textos = []
classe = []


tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)

def tratamentoTexto (texts):
	texto = tokenizer.tokenize(texts.translate(translator).lower())
	texto = [p for p in texto if p not in stopwordsnltk]
	texto = [str(stemmer.stem(p)) for p in texto]
	return texto


with open("textos.tsv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter="\t")
	for i in reader:
		textos.append(tratamentoTexto(i[1]))
		classe.append(i[0])
	print(textos)
	#print(classe)



dictionario = corpora.Dictionary(textos)


with open("textos.tsv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter="\t")
	atributos = []
	for j in reader:
		atr = tratamentoTexto(j[1])
		bow = dictionario.doc2bow(atr)
		temp = [0 for x in range (len(dictionario)+1)]
		for endereco,freq in bow:
			temp[endereco] = freq
		temp[-1] = j[0] 
		atributos.append(temp)
	print(atributos)

with open ("BOW.csv", "w", newline='') as csvFile:
	spamWriter = csv.writer(csvFile, delimiter=",")
	for j in atributos:
		spamWriter.writerow(j) 

