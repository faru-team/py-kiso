# list-要素数と値の出現位置
# len()関数でリストの要素の数を取得する
names = ["東京","埼玉","神奈川"]
print(len(names))

# count()メソッドで値の出現回数を取得する
names = ["王","東京","埼玉","神奈川"]
print(names.count("埼玉"))

# index()メソッドで値が最初に出現する位置を取得する
names = ["王","兵","東京","埼玉","神奈川"]
print(names.index("神奈川"))