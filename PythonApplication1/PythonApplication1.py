import numpy as np
from itertools import permutations
import random
from GUI import Board
from StarConstructor import StarConstructor


class StarBattle:
    def __init__(self, size, starcount=1, cMet='random'):
        self.stars=starcount
        self.size=size
        self.cMet=cMet
        if self.cMet == 'random':
            self.randConstructor()
        else:
            self.detConstructor(self.cMet)

        self.islandConstructor()

    def randConstructor(self):
        self.strc=np.eye(self.size,dtype=int)
        while not self.isValid(self.strc):
            print(self.strc)
            self.strc=np.eye(self.size,dtype=int)
            while not self.isValid(self.strc):
                self.strc=np.random.permutation(self.strc)
            temp=np.eye(self.size,dtype=int)
            for i in range(1,self.stars):
                while not self.isValid(temp):
                        temp=np.random.permutation(temp)
                self.strc=np.add(self.strc,temp)
    
    def detConstructor(self,cMet):
        self.strc=np.eye(self.size,dtype=int)
        self.strc=self.strc[cMet]
        if not self.isValid(self.strc):
            pass

    def islandConstructor(self):
        self.islands=np.zeros((self.size,self.size),dtype=int)
        t=1
        for x in np.ndindex(np.shape(self.strc)):
            if self.strc[x] == 1:
                self.islands[x]=t
                t+=1
        while np.isin(self.islands,0).any()==True:
            for x in np.ndindex(np.shape(self.strc)):    
                if self.islands[x]==0:
                    Y=self.islands[max(x[0]-1,0):min(x[0]+2,self.size),max(x[1]-1,0):min(x[1]+2,self.size)]
                    for t in range(1,self.size+1):
                        R=random.choice((0,1,2))
                        if np.isin(Y,t).any() and R==1:
                            self.islands[x]=t

    def isValid(self,X):
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


Star = StarConstructor(size=11, star_count=1)
Star.construct_field()
# Star.isValid(Star.board)
# board = Board(np.zeros(np.array(Star.strc).shape), Star.strc, Star.islands)
# board.show()
