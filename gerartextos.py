import nltk
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora
import csv
import string
  

translator = str.maketrans('', '', string.punctuation)

txt1=[]
txt2=[]

with open("Paralelo.tsv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter="\t")
	for i in reader:
		txt1.append(i[1])
with open("Formulário.tsv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter="\t")
	for i in reader:
		txt2.append(i[2])


#print(len(txt2))
'''w = [len(word) for line in txt1 for word in line] #contagem de caracteres
wp = [len(line) for line in txt1]
w_avg = sum(w)/len(wp) #characteres'''

with open("textos.tsv", "w", encoding='utf8', newline="") as csvFile:
	spamwriter = csv.writer(csvFile, delimiter= "\t", quotechar = '"', quoting = csv.QUOTE_NONNUMERIC) 
	for i in txt1:
		spamwriter.writerow([1, i.translate(translator)])
		#print ([1, i.translate(translator)])
	for i in txt2:
		spamwriter.writerow([0, i.translate(translator)])
		#([1, i.translate(translator)])


