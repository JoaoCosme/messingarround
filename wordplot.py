import matplotlib.pyplot as plt
import numpy as np

dicionario = []
PATH = "palavras.txt"
alfabeto = "abcdefghijklmnopqrstuwvxyz"
alfabetoDict = {}

for i in range(len(alfabeto)):
    alfabetoDict[alfabeto[i]]=0


with open(PATH,"r",encoding="utf8") as arq:
    dicionario = [word for word in arq]

for word in dicionario:
    if word[0] in alfabetoDict:
        alfabetoDict[word[0]]+=1


index = np.arange(len(alfabeto))
plt.bar(index, alfabetoDict.values())
plt.xlabel('Letra', fontsize=10)
plt.xticks(index, alfabetoDict.keys(), fontsize=10)
plt.ylabel('No de Letras ', fontsize=5)
plt.show()

