
from scipy.spatial.distance import euclidean
import pandas as pd

data = [pd.read_csv("data/data/data0.csv", index_col=False,header=None), pd.read_csv("data/data/data1.csv", index_col=False,header=None),
        pd.read_csv("data/data/data2.csv", index_col=False,header=None), pd.read_csv("data/data/data3.csv", index_col=False,header=None),
        pd.read_csv("data/data/data4.csv", index_col=False,header=None), pd.read_csv("data/data/data5.csv", index_col=False,header=None),
        pd.read_csv("data/data/data6.csv", index_col=False,header=None), pd.read_csv("data/data/data7.csv", index_col=False,header=None)]

#ユークリッド距離を返す
def calc(data1,data2):
    summ=0
    for i in range(5):
        for j in range(5):
            summ += euclidean(data1.iat[i,j],data2.iat[i,j])
    return summ

sumlist = [0,0,0,0,0,0,0,0]
for k in range(8):
    for l in range(8):
        sum1 = calc(data[k], data[l])
        sumlist[k]+=sum1
print("data",sumlist.index(min(sumlist)))
answer = pd.core.frame.DataFrame(sumlist)
answer.to_csv('./answer.csv', index=False, header=False)
