#encoding=utf-8
import pandas as pd
import numpy as np
from matplotlib import cm
from matplotlib import axes
from matplotlib import pyplot as plt
#Draw heatmap
def draw_heatmap(data,xlabels,ylabels):
    cmap = cm.Blues
    figure=plt.figure(facecolor='w')
    ax=figure.add_subplot(1,1,1)#,position=[0.1,0.15,0.8,0.8])
    if ylabels:
        ax.set_yticks(range(len(ylabels)))
        ax.set_yticklabels(ylabels)
    if xlabels:
        ax.set_xticks(range(len(xlabels)))
        ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    map=ax.imshow(data,interpolation='nearest',cmap=cmap,vmin=0,vmax=1)
    cb=plt.colorbar(mappable=map,cax=None,ax=None,shrink=0.5)
    plt.show()
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