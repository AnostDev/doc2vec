from source import cosineFile as cosine
import os

k = 1

repoTrain = "/home/chriss/Desktop/Semestre6/tal/tp3/TP02-textclassif/train/"

def categorize(A):
    tableau = {}
    for filename in os.listdir(repoTrain):
        a=  cosine(A, filename)
        print(str(a))
        #tableau[filename] = cos(A, filename)




categorize("/home/chriss/Desktop/Semestre6/tal/tp3/TP02-textclassif/test/10.txt")