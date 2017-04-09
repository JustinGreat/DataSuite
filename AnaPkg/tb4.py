#encoding=utf-8
from data_analysis import *
import scipy
from scipy.stats import chisquare

class Tb4Ana(DataAnaClass):
    data=""
    def __init__(self,data):
        if not data.shape[0]==2 and data.shape[1]==2:
            print("Warning:TB4 shape is wrong!")
            return
        self.data=data
    def processData(self):
        #Return ChiSquare
        if not self.data.any():
            return np.nan
        a=self.data[0][0]
        b=self.data[0][1]
        c=self.data[1][0]
        d=self.data[1][1]
        s=a+b+c+d
        return s*(a*d-b*c)**2/((a+b)*(a+c)*(b+d)*(c+d))
def main():
    d=np.array([[19.0,24.0],[34.0,10.0]])
    x=Tb4Ana(d)
    print x.processData()
if __name__=="__main__":
    main()
