import pandas as pd

inf = pd.read_csv("hoge.csv",index_col=False,header=None)
#outf = pd.read_csv("hogehoge.csv", index_col=0)

for i in range(3):
    for j in range(3):
        inf.iat[i,j] +=1

print(type(inf))

inf.to_csv('./hogehoge.csv',index=False,header=False)