from source import doc2vec as dv
import math as m

pathA = "1rst file"
pathB = "second file"

a = dv.vec(pathA)
b = dv.vec(pathB);


def scalaire(A,B):
    ret =0
    for occ in A:
        if B.__contains__(occ):
            print(occ)
            ret = ret+  A[occ] * B[occ]

    return ret

def dist_eclu(A):
    tmp = 0
    for occ in A:
        tmp = tmp + pow(A[occ], 2)
    return m.sqrt(tmp)


def cosine(A, B):
    return scalaire(A,B)/(dist_eclu(A)*dist_eclu(B))


print(cosine(a,b))


