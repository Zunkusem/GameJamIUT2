from math import *
class Time():

    def __init__(self):
        self.minutes=3
        self.secondes=0
        self.milli=0

    def incremente(self):
        if self.milli <=0:
            self.secondes=self.secondes-1
            self.milli=999
        if self.secondes<= 0:
            self.minutes=self.minutes-1
            self.secondes=59
        self.milli=self.milli-(1/60)*1000

    def get(self):
        #return(str(self.minutes)+":"+str(self.secondes)+":"+str(round(self.milli,-1)))
        if self.secondes >9:
            sec = str(self.secondes)
        else :
            sec="0"+str(self.secondes)
        return(str(self.minutes)+":"+sec+":"+str(int(round(self.milli,-1))))

    def estFini(self):
        #print(self.milli," ",self.secondes," ",self.minutes)
        if self.minutes <0 :
            #print("True")
            return True
        else:
            #print("False")
            return False
