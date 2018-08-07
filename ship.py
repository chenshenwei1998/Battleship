#Ship.py
from random import *

typedict={1:'ROWBOAT',2:'SUBMARINE',3:'SPEEDBOAT',4:'BATTLESHIP',5:'LONGBOAT'}

def matrix():
    matrix=[]
    for i in range(10):
        temp=[]
        for i in range(15):
            temp.append(0)
        matrix.append(temp)
    return matrix

def setup(matrix,x,y,later):
    matrix[x-1][y-1]=later
    
    
    
            
            
class Ship():
    def __init__(self,type1,state,startline,startcolumn):
        self.type1=type1
        self.state=state
        self.line=startline
        self.column=startcolumn

    def setship(self):
        if self.state==1:
            for i in range(self.type1):
                setup(Mat,self.line,self.column+i,self.type1)
        else:
            for i in range(self.type1):
                setup(Mat,self.line+i,self.column,self.type1)

    def setshipID(self):
        if self.state==1:
            for i in range(self.type1):
                setup(MatID,self.line,self.column+i,[self.line,self.column,self.type1,self.state,self.type1])
        else:
            for i in range(self.type1):
                setup(MatID,self.line+i,self.column,[self.line,self.column,self.type1,self.state,self.type1])
        
                
    def judge(self,line,column):
        if self.state==1:
            for i in range(self.type1):
                if column + self.type1 - 1<=15:
                    if Mat[line-1][column+i-1]==0:
                        pass
                    else:
                        return False
                else:
                    return False
            return True
        else:
            for i in range(self.type1):
                if line+self.type1-1<=10:
                    if Mat[line+i-1][column-1]==0:
                        pass
                    else:
                        return False
                else:
                    return False
            return True
        
    


def randship(numbers):
    global Mat
    Mat=matrix()
    global MatID
    MatID=matrix()
    global allship
    allship={1:0,2:0,3:0,4:0,5:0}
    for i in range(numbers):
        type1=randint(1,5)
        state=randint(1,2)
        startline=randint(1,10)
        startcolumn=randint(1,15)
        flag=1
        ship=Ship(type1,state,startline,startcolumn)
        while flag:
            if ship.judge(startline,startcolumn):
                allship[type1]+=1
                ship.setship()
                ship.setshipID()
                flag=0
            else:
                startline=randint(1,10)
                startcolumn=randint(1,15)
                ship=Ship(type1,state,startline,startcolumn)
    return Mat,MatID,allship

#test

            
    






    
        
        
        
        
