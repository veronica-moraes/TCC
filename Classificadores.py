import csv
import numpy as np
from sklearn.model_selection import KFold, cross_val_score, StratifiedKFold 
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity


atributos = []
classe = []
lb = LabelBinarizer()

with open("BOW.csv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter=",")
	for i in reader:
		atributos.append(i[:len(i)-1])
		classe.append(i[-1])


'''with open("liwc.csv", encoding='utf8', newline="") as csvFile:
	reader = csv.reader(csvFile, delimiter=",")
	for i in reader:
		atributos.append(i[:len(i)-1])
		classe.append(i[-1])

'''
X = np.array(atributos) 
y = np.array([number[0] for number in lb.fit_transform(classe)]) 
kf = StratifiedKFold(n_splits=5) 
kf.get_n_splits(X) 


rf_class = RandomForestClassifier(random_state = 0)
svm_class = svm.SVC(kernel=cosine_similarity)

accuracy = cross_val_score(rf_class, X, y, scoring='accuracy', cv = kf).mean() * 100
print("Accuracy of Random Forests is: " , accuracy)
precision = cross_val_score(rf_class, X, y, scoring='precision', cv = kf).mean() * 100
print("Precision of Random Forests is: " , precision)
recall = cross_val_score(rf_class, X, y, scoring='recall', cv = kf).mean() * 100
print("Recall of Random Forests is: " , recall)
f1 = cross_val_score(rf_class, X, y, scoring='f1', cv = kf).mean() * 100
print("F1 of Random Forests is: " , f1)
print("-"*200)


accuracy = cross_val_score(svm_class, X, y, scoring='accuracy', cv = kf).mean() * 100
print("Accuracy of SVM is: " , accuracy)
precision = cross_val_score(svm_class, X, y, scoring='precision', cv = kf).mean() * 100
print("Precision of SVM is: " , precision)
recall = cross_val_score(svm_class, X, y, scoring='recall', cv = kf).mean() * 100
print("Recall of SVM is: " , recall)
f1 = cross_val_score(svm_class, X, y, scoring='f1', cv = kf).mean() * 100
print("F1 of SVM is: " , f1)

