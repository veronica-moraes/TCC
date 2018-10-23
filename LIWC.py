import csv
import string
from nltk.tokenize import TweetTokenizer
import liwc
from collections import Counter

translator = str.maketrans('', '', string.punctuation)
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)

parse, category_names = liwc.load_token_parser('LIWC2007_Portugues_win.dic2')

classe = []
atr = []
# Funções

def tratamentoTexto(text):
    texto = tknzr.tokenize(text.translate(translator).lower())
    #texto = [x for x in texto if x not in STOP]
    #texto = [lmtz.lemmatize(x) for x in texto]
    #texto = [SnowballStemmer("english").stem(x) for x in texto]
    return texto

with open("textos.tsv",encoding='utf8', newline="") as csvFile:
    reader = csv.reader(csvFile, delimiter="\t")
    #temp = [0 for n in range(len(category_names)+1)]

    
    with open("liwc.csv","w",newline="") as salva:
        spamwriter = csv.writer(salva,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
        for i in reader:
            temp = [0 for n in range(len(category_names)+1)]
            teste_counts = Counter(category for token in tratamentoTexto(i[1]) for category in parse(token))
            z = 0
            #print(teste_counts)
            for x in category_names:
                #temp[z] = round(teste_counts[x]/sum(teste_counts.values()),4)
                temp[z] = teste_counts[x]
                z+=1
                #print(temp)
            temp[len(category_names)] = i[0]

            print(temp)
            spamwriter.writerow(temp)



