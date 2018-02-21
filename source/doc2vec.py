# -*- coding: UTF8 -*-

import os
import sys
import operator
import codecs


pathStop = "stop word file"


def vec(file):



    testFile = file

    current_s_file = open(pathStop, "r")
    tmp_stop = current_s_file.read()
    stop_word = tmp_stop.split("\n")  # stop word
    #  print(stop_word)

    with open(testFile, "r") as current_file:
        tmpFile = current_file.read() # attention à l'encodage
        current_file.close()
        str = tmpFile.split(" ")  # recuperation de la chaine de caractère
        str.sort()
        vec = {}

        for ch in str:
            # if (ch.__len__() > 1 ): #suppression des chaines de caractères à une lettre
            vec[ch] = str.count(ch)  # dictionnaire


        for tp in stop_word:  # filtrage des stopwords
            if vec.__contains__(tp):
                del vec[tp]

        return vec

        # tri en fonction du nombre d'occurrence



def sortedVec(A):
    sortedVec = sorted(A.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples
    return sortedVec

# generation des représentation vectorielles de tous les fichiers
# a revoir probleme de codecs et de permission
# si non tout semble etre correct
def write_vec(file):

    try :
         os.mkdir(file+"vec", 0o777)
    except FileExistsError:
        print("dossier existant")

    repo = "Train repository"

    for filename in os.listdir(repo):
        #print(filename)
        vecName = filename.strip('.txt')
        vecName = file + "vec/" +'' + vecName + ".vec"

        print(vecName)
        dv = vec(repo + '' + filename)
        dv_sorted = sortedVec(dv)

        try:
            with codecs.open(vecName, 'w', 'utf-8') as dvFile:

                for tup in dv_sorted:
                    tmp = ''
                    tmp = str(tup[0]) + "\t" + str(tup[1])+ "\n"
                    dvFile.write(tmp)
                #dvFile.write(s)
        except PermissionError:
            print('permission denied')
        except UnicodeDecodeError:
            pass




# a = vec("file path" )

# write_vec("resource repos, where to write .vec files")