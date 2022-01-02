'''
Created on 2021年12月19日

@author: Konic
'''

'''
Eulicid method to get the maximum common factor
'''
def gcd(m,n):
    while m%n!=0:
        oldm=m
        oldn=n
        m=oldn
        n=oldm%oldn
    return n
'''
a class for fratcion and implement the function of print, simplify,add and compare whether it is the same as the other fraction
'''
class Fraction(object):
    '''
    classdocs
    '''


    def __init__(self, num,den):
        '''
        Constructor
        '''
       
        
        if type(num)!= int or type(den)!=int:
            raise ValueError
        if den<0:
            num=-num
        com=gcd(num,den)
        self.num=num//com
        self.den=den//com
    def __str__(self):
        
        
        return str(self.num)+'/'+str(self.den)

    def __add__(self,fractionb):
        newnum=self.num*fractionb.den+ \
        self.den*fractionb.num
        newden=self.den*fractionb.den
#         com=gcd(newnum,newden)
        return Fraction(newnum,newden)
    
    def __eq__(self,fractionb):
        numa=self.num*fractionb.den
        numb=fractionb.num*self.den
        return numa==numb
    def __sub__(self,fractionb):
        newnum=self.num*fractionb.den- \
        self.den*fractionb.num
        newden=self.den*fractionb.den
        return Fraction(newnum,newden)
    def getnum(self):
        return self.num
    def getden(self):
        return self.den
    
a=Fraction(3,5)
b=Fraction(6,10)
print(b)
    
    


class logicgate:
    def __init__(self,n):
        self.label=n
        self.output=None
    def getlabel(self):
        return self.label
    
    def getoutput(self):
        self.output=self.function()
        return self.output
    def setNextPin(self,source):
        if self.pina==None:
            self.pina=source
        else:
            if self.pinb==None:
                self.pinb=source
            else:
                raise RuntimeError('no empty pin')
class bigate(logicgate):
    def __init__(self,n):
        super().__init__(n)
        self.pina=None
        self.pinb=None
        
    def getpina(self):
        if self.pina==  None:
            
            return int(input('enter pinA for gate'+self.getlabel()+'--->'))
        else:
            return self.pina.getfgate().getoutput()
    def getpinb(self):
        if self.pinb==None:
            return int(input('enter pinB for gate'+self.getlabel()+'--->'))
        else:
            return self.pinb.getfgate().getoutput()
    
class unigate(logicgate):
    def __init__(self,n):
        super().__init__(n)
        self.pin=None
    def getpin(self):
        return int(input('enter pin for gate'+self.getlabel()+'--->'))
    

class andgate(bigate):
    def __init__(self,n):
        super().__init__(n)
    def function(self):
        a=self.getpina()
        b=self.getpinb()
        if a==1 and b==1:
            return 1
        else:
            return 0
        
class orgate(bigate):
    def __init__(self,n):
        super().__init__(n)
    def function(self):
        a=self.getpina()
        b=self.getpinb()
        if a==0 and b==0:
            return 0
        else:
            return 1
        
class notgate(unigate):
    def __init__(self,n):
        super().__init__(n)
        
    def function(self):
        s=self.getpin()
        if s==0:
            return 1
        else:
            return 0
    def setNextPin(self,source):
        if self.pin==None:
            self.pina=source
        
        else:
            raise RuntimeError('no empty pin')
        
class connector:
    def __init__(self,fgate,tgate):
        self.fgate=fgate
        self.tgate=tgate
        tgate.setNextPin(self)
    def getfgate(self):
        return self.fgate
    def gettgate(self):
        return self.tgate
        
g1=andgate('g1')
g2=andgate('g2')
g3=orgate('g3')
g4=notgate('g4')
c1=connector(g1,g3)
c2=connector(g2,g3)
c3=connector(g3,g4)

a=g4.getoutput()
print(a)