import numpy as np
from itertools import permutations
import random

class StarBattle():
    def __init__(self,size,starcount=1,cMet='random'):
        self.stars=starcount
        self.size=size
        self.cMet=cMet
        if type(self.cMet)==np.ndarray:
            self.detConstructor(self.cMet)
        else:
            self.randConstructor()

        #self.islandConstructor()

    def randConstructor(self):  
        self.strc=np.eye(self.size,dtype=int)
        while not self.isValid(self.strc): ### prob isValid returns True on np.random.permutation approaches e^-2 as n tends to infinity
            self.strc=np.eye(self.size,dtype=int)
            while not self.isValid(self.strc):
                self.strc=np.random.permutation(self.strc)
            temp=np.eye(self.size,dtype=int)
            for i in range(1,self.stars):  ### empirical testing: n=10 ca 1/80000-1/300000 n=20 ca 1/20000-1/40000 for 2 stars (not efficient)
                while not self.isValid(temp):
                        temp=np.random.permutation(temp)
                self.strc=np.add(self.strc,temp)
    def detConstructor(self,cMet):
        self.strc=np.eye(self.size,dtype=int)
        self.strc=self.strc[cMet]
        if not self.isValid(self.strc):
            pass

    def islandConstructor(self, diag=False):
        self.islands=np.zeros((self.size,self.size),dtype=int)
        t=1
        for x in np.ndindex(np.shape(self.strc)):
            if self.strc[x] == 1:
                self.islands[x]=t
                t+=1
        while np.isin(self.islands,0).any()==True:
            for x in np.ndindex(np.shape(self.strc)):    
                if self.islands[x]==0:
                    if diag:
                        Y=self.islands[max(x[0]-1,0):min(x[0]+2,self.size),max(x[1]-1,0):min(x[1]+2,self.size)]
                    else:
                        Y=[]
                        if x[0]+1<=self.size-1: Y.append(self.islands[(x[0]+1,x[1])])
                        if x[0]-1>=0:Y.append(self.islands[(x[0]-1,x[1])])
                        if x[1]+1<=self.size-1:Y.append(self.islands[(x[0],x[1]+1)])
                        if x[1]-1>=0:Y.append(self.islands[(x[0],x[1]-1)])
                    for t in range(1,self.size+1):
                        R=random.choices((0,1),weights=[self.size,1],k=1)[0]
                        if np.isin(Y,t).any() and R==1:
                            self.islands[x]=t
        for st in range(1,self.stars):
            print('hello')

    def isValid(self,X):
        for index in np.ndindex(np.shape(X)):
            if X[index]==1:
                for epi in (-1,1):
                    for epj in (-1,1):
                            if self.size-1>=index[0]+epi>=0 and self.size-1>=epj+index[1]>=0 and not (epi==epj and epi==0) and not X[index[0]+epi,index[1]+epj]==0:
                                self.Valid = False
                                return self.Valid
        if (X.sum(axis=0)==self.stars).all() and (X.sum(axis=1)==self.stars).all() and np.amax(X)==self.stars:
            self.Valid = True
        else:
            self.Valid = False
        return self.Valid


    def isValid1(self,X):
        for index in np.ndindex(np.shape(X)):
            if X[index]==1:
                for epi in (-1,0,1):
                    for epj in (-1,0,1):
                            if self.size-1>=index[0]+epi>=0 and self.size-1>=epj+index[1]>=0 and not (epi==epj and epi==0) and not X[index[0]+epi,index[1]+epj]==0:
                                self.Valid = False
                                return self.Valid
            elif X[index]>1:
                self.Valid = False
                return self.Valid
        self.Valid = True
        return self.Valid


def test():
    import matplotlib.pyplot as plt

    x=StarBattle(50,starcount=2)
    #print(x.islands)
    #input()
    print(x.strc)

    plt.imshow(x.islands)
    plt.show()

def testisValid():
    Y=[]
    import time
    import matplotlib.pyplot as plt

    for i in range(1,100):
        G=np.zeros((100))
        for j in range(0,100):
            X=np.random.permutation(i)
            t=time.time()
            StarBattle(i,cMet=X)
            t=time.time()-t
            G[j]=t
        Y.append(G.sum()/100)
    plt.plot(Y)
    plt.show()
    
