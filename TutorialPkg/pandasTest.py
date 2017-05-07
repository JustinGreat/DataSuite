#encoding=utf-8
import numpy as np
import pandas as pd

def main():
    #Data Structure
    s=pd.Series([i*2 for i in range(1,11)])
    print(type(s))
    dates=pd.date_range("20170301",periods=8)
    df=pd.DataFrame(np.random.randn(8,5),index=dates,columns=list("ABCDE"))
    print(df)
    #df=pd.DataFrame({"A":1,"B":pd.Timestamp("20170301"),"C":pd.Series(1,index=list(range(4)),dtype="float32"),\
    #   "D":np.array([3]*4,dtype="float32"),"E":pd.Categorical(["police","student","teacher","doctor"])})
    #print(df)

    #Basic
    print(df.head(3))
    print(df.tail(3))
    print(df.index)
    print(df.values)
    print(df.T)
    print(df.sort(columns="C"))
    print(df.sort_index(axis=1,ascending=False))
    print(df.describe())
    print(df.sample())
    #Select
    print(type(df["A"]))
    print(df[:3])
    print(df["20170301":"20170304"])
    print(df.loc[dates[0]])
    print(df.loc["20170301":"20170304",["B","D"]])
    print(df.at[dates[0],"C"])

    print(df.iloc[1:3,2:4])
    print(df.iloc[1,4])
    print(df.iat[1,4])

    print(df[df.B>0][df.A<0])
    print(df[df>0])
    print(df[df["E"].isin([1,2])])

    #Set
    s1=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))
    df["F"]=s1
    print(df)
    df.at[dates[0],"A"]=0
    print(df)
    df.iat[1,1]=1
    df.loc[:,"D"]=np.array([4]*len(df))
    print(df)
    df2=df.copy()
    df2[df2>0]=-df2
    print(df2)

    #Missing Values
    df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])
    df1.loc[dates[0]:dates[1],"G"]=1
    print(df1)
    print(df1.dropna())
    print(df1.fillna(value=2))

    #Statistic
    print(df.mean())
    print(df.var())
    print(df.corr(method="spearman"))
    s = pd.Series([1, 2, 2, np.nan, 5, 7, 9, 10], index=dates)
    print(s)
    print(s.corr(s))
    print(s.shift(2))
    print(s.diff())
    print(s.value_counts())
    print(df.apply(np.cumsum))
    print(df.apply(lambda x:x.max()-x.min()))

    #Concat
    pieces=[df[:3],df[-3:]]
    print(pd.concat(pieces))
    left=pd.DataFrame({"key":["x","y"],"value":[1,2]})
    right=pd.DataFrame({"key":["x","z"],"value":[3,4]})
    print("LEFT:",left)
    print("RIGHT:",right)
    print(pd.merge(left,right,on="key",how="outer"))
    df3 = pd.DataFrame({"A": ["a", "b", "c", "b"], "B": list(range(4))})
    print(df3.groupby("A").sum())

    #Reshape
    import datetime
    df4 = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                       'B': ['a', 'b', 'c'] * 8,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                       'D': np.random.randn(24),
                       'E': np.random.randn(24),
                       'F': [datetime.datetime(2017, i, 1) for i in range(1, 13)] +
                            [datetime.datetime(2017, i, 15) for i in range(1, 13)]})
    print(pd.pivot_table(df4,values="D",index=["A","B"],columns=["C"]))


    #Time Series
    t_exam=pd.date_range("20170301",periods=10,freq="S")
    print(t_exam)

    #Graph
    ts=pd.Series(np.random.randn(1000),index=pd.date_range("20170301",periods=1000))
    ts=ts.cumsum()
    from pylab import *
    ts.plot()
    show()

    #File
    df6=pd.read_csv("./data/test.csv")
    print(df6)
    df7=pd.read_excel("./data/test.xlsx","Sheet1")
    print("Excel",df7)
    df6.to_csv("./data/test2.csv")
    df7.to_excel("./data/test2.xlsx")

if __name__=="__main__":
    main()