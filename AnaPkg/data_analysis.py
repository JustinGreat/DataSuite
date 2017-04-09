#encoding=utf-8
import pandas as pd
import numpy as np
class DataAnaClass():
    def preProcess(self):
        pass
    def processData(self):
        pass
    def predictRes(self):
        pass
    def evaluateRes(self):
        pass
class PdExpand():
    ds=""
    def __init__(self,data):
        self.ds=data
    #dispersion coefficience
    def dispcoef(self,axis=0):
        return self.ds.std(axis=axis)/self.ds.mean(axis=axis)
    #sk coefficience
    def sk(self):
        if not isinstance(self.ds,pd.core.series.Series):
            print("Warning:data structure is not right!")
            return 0.0
        if self.ds.size<3:
            print("Warning:data size < 3!")
            return 0.0
        num=float(self.ds.size)
        s3=self.ds.std()**3
        m3s=np.sum((self.ds.values-self.ds.mean())**3)
        print (self.ds.values-self.ds.mean())**3
        return num/(num-1)/(num-2)*m3s/s3
    #peak coefficience
    def pk(self):
        if not isinstance(self.ds, pd.core.series.Series):
            print("Warning:data structure is not right!")
            return 0.0
        if self.ds.size < 4:
            print("Warning:data size < 4!")
            return 0.0
        num=float(self.ds.size)
        s4=self.ds.std()**4
        s4m=np.sum((self.ds.values-self.ds.mean())**4)
        return num*(num+1)/(num-1)/(num-2)/(num-3)*s4m/s4-3*(num-1)**2/(num-2)/(num-3)
def main():
    empl=PdExpand(pd.Series([1,3,9,3,1]))
    print(empl.sk())
    print(empl.pk())

if __name__=="__main__":
    main()