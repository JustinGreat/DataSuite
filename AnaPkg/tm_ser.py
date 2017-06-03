#encoding=utf-8
from data_analysis import *
from pylab import *
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
class TimeSeqClass(DataAnaClass):
    def __init__(self,data):
        self.data=""
        self.arma_mod=""
        if not isinstance(data, pd.core.series.Series):
            print("WARNING:Data type is not Series.")
        self.data=data
    def preProcess(self,diffn=1):
        from statsmodels.tsa.stattools import adfuller
        adf_res = adfuller(self.data.values)
        print("ADF:",adf_res)
        lag = 40
        fig = figure(figsize=(12, 8))
        ax1 = fig.add_subplot(211)
        fig = sm.graphics.tsa.plot_acf(self.data.diff(diffn)[diffn:], lags=lag, ax=ax1)
        ax2 = fig.add_subplot(212)
        fig = sm.graphics.tsa.plot_pacf(self.data.diff(diffn)[diffn:], lags=lag, ax=ax2)
        show()
    def processData(self,p,q):
        self.arma_mod = sm.tsa.ARMA(self.data, (p,q)).fit()
        print("AIC:",str(self.arma_mod.aic))
        print("BIC:",str(self.arma_mod.bic))
        print("HQIC:",str(self.arma_mod.hqic))
        resid = self.arma_mod.resid
        print("DW value:",sm.stats.durbin_watson(resid.values))
        fig = figure(figsize=(12, 8))
        ax1 = fig.add_subplot(311)
        fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
        ax2 = fig.add_subplot(312)
        fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
        ax = fig.add_subplot(313)
        fig = qqplot(resid, line='q', ax=ax, fit=True)
        show()
    def predictRes(self,prd_start,prd_end):
        predict_sunspots = self.arma_mod.predict(prd_start,prd_end, dynamic=True)
        print("Predict:",predict_sunspots)
        fig, ax = subplots(figsize=(12, 8))
        ax = self.data.ix.plot(ax=ax)
        predict_sunspots.plot(ax=ax, color="red")
        show()
def main():
    pass

if __name__=="__main__":
    main()