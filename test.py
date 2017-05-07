#encoding=utf-8
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #print np.random.random([4,4])
    sns.heatmap(np.corrcoef(np.random.randn(10,10)))
    plt.show()
if __name__=="__main__":
    main()