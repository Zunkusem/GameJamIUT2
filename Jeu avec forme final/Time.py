from math import *
class Time():

    def __init__(self):
        self.minutes=0
        self.secondes=0
        self.milli=0

    def incremente(self):
        self.milli=self.milli+(1/60)*1000
        if self.milli>999:
            self.secondes=self.secondes+1
            self.milli=self.milli-1000
        if self.secondes>59:
            self.minutes=self.minutes+1
            self.secondes=self.secondes-60

    def get(self):
        #return(str(self.minutes)+":"+str(self.secondes)+":"+str(round(self.milli,-1)))
        return(str(self.minutes)+":"+str(self.secondes)+":"+str(int(round(self.milli,-1))))
