#encoding=utf-8
from data_analysis import *
from sklearn.decomposition import PCA
class PcaAnaClass(DataAnaClass):
    data=[]
    def __init__(self,data):
        self.data=data
    def processData(self,n,cmd="cov"):
        if not cmd in ["cov","corr"]:
            print("CMD Error!")
        if cmd=="corr":
            pca = PCA(n_components=n)
            new_data=pca.fit_transform(self.data)
            return new_data,pca.explained_variance_ratio_
        if cmd=="cov":
            meanVals = np.mean(self.data, axis=0)
            DataAdjust = self.data - meanVals
            covMat = np.cov(DataAdjust, rowvar=0)
            eigVals, eigVects = np.linalg.eig(np.mat(covMat))
            eigValInd = np.argsort(eigVals)
            eigValInd = eigValInd[:-(n + 1):-1]
            redEigVects = eigVects[:, eigValInd]
            lowDDataMat = DataAdjust * redEigVects
            # reconMat = (lowDDataMat * redEigVects.T) + meanVals
            return lowDDataMat, eigValInd


def main():
    pass
if __name__=="__main__":
    main()