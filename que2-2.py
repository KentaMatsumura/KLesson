import csv

#問題点：読みだしたとき、文字列になっている！！！！

with open('hoge.csv', 'r', newline='') as inf:
    with open('hogehoge.csv', 'w', newline='')as outf:
        #読み込みファイルと書き込みファイルのオブジェクト作成
        reader = csv.reader(inf)
        writer = csv.writer(outf)
        #読み込みファイルの文字列を数値に変換
        data = [[int(elm) for elm in v] for v in reader]
        for i in range(len(data[0])):#行
            for j in range(len(data[0])):#列
                data[i][j]+=1
            writer.writerow(data[i])#書き込み
