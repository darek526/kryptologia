#!/userbin/env /usr/bin/python3

def szyfrowanie(TJ,K,SZ):
    L=int(TJ[0:8],2)
    P=int(TJ[8:],2)
    K=int(K,2)
    L1 = P
    P1=L^(P^K)
    temp_L1=str(bin(L1))
    temp_P1=str(bin(P1))
    temp_L1=temp_L1[2:]
    if len(temp_L1)<8:
        temp_L1="0"*(8-len(temp_L1))+temp_L1
    temp_P1=temp_P1[2:]
    if len(temp_P1)<8:
        temp_P1="0"*(8-len(temp_P1))+temp_P1
    SZ=temp_L1+temp_P1
    return SZ

def deszyfrowanie(SZ2,K,TJ2):
    L1=int(SZ2[0:8],2)
    P1=int(SZ2[8:],2)
    K=int(K,2)
    P=L1
    L=P1^(L1^K)
    temp_L=str(bin(L))
    temp_P=str(bin(P))
    temp_L=temp_L[2:]
    if len(temp_L)<8:
        temp_L="0"*(8-len(temp_L))+temp_L
    temp_P=temp_P[2:]
    if len(temp_P)<8:
        temp_P="0"*(8-len(temp_P))+temp_P
    TJ2=temp_L+temp_P
    return TJ2
