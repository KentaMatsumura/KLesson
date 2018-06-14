from scipy.spatial.distance import euclidean
import pandas as pd
import glob
import numpy as np

# 指定したディレクトリ内のcsvファイルのパスを代入
file = glob.glob("data/data/*.csv")
# csvファイルを代入するリストを初期化
# len():リストの要素数をカウント
count = len(file)
#csvファイルの代入するリストの初期化
filecsv = [0 for i in range(count)]

# csvファイルを代入
for i in range(count):
    filecsv[i] = pd.read_csv(file[i], index_col=False, header=None)


# ユークリッド距離の合計を返す
def calc(data1, data2):
    summ = 0
    for i in range(5):
        for j in range(5):
            # 要素ごとのユークリッド距離を加算
            summ += euclidean(data1.iat[i, j], data2.iat[i, j])
    return int(summ)

# 各csvファイルのユークリッド距離の合計を代入するリストの初期化
sumlist2 = np.ones([8,8], dtype=int)

for k in range(8):
    for l in range(8):
        # ユークリッド距離の合計をリストに代入
        #sumlist[k] = calc(filecsv[k], filecsv[l])
        sumlist2[k][l] = calc(filecsv[k], filecsv[l])



# ユークリッド距離の最小を抽出
for i in range(8):
    summin = np.argmin(sumlist2[i])
    #最小値が０の場合、それを1000にする
    sumlist2[i,i]=1000
    #ユークリッド距離が最も小さい組み合わせとその値を表示
    print("data",i,".csv  ->","data",summin,".csv", sumlist2[i,summin])
