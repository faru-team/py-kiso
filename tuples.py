# タプルとは、変更できないリストのこと
# タプルは一度定義すると
# 要素の追加、削除、並び替え、値の変更ができない

names = ("王","兵","東京","埼玉","神奈川")
names_list = ["王"]
print(type(names_list))

not_tuple = ("王")
print(type(not_tuple))

names_tuple = ("王",)
print(type(names_tuple))
# not_tupleのタイプはstrのまま、names_tupleが「,」を付けることで
# typeがtupleになる

# 要素へアクセス、要素数の取得、値の出現回数の取得
# 値が最初に出現する位置の取得はリストと同じ
names = ("王","皇族","王族","貴族")
print(names[0])
print(len(names))
print(names.count("王族"))
print(names.index("王族"))

# タプルには、copy()メソッドもextend()メソッドがありません
# +演算子によるタプル結合する
names = ("Naruto","Sasuke","Sakura","Hinata")
names1 = ("rasengan","syaringan","ouka","byakugan")
names2 = names + names1
print(names2)
