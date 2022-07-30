# list-コピー結合
names1 = ["naruto","sasuke","kakasi","hinata"]
names2 = names1

names2[0] = "madara"
print(names1)
print(names2)

names1[0] = "hasirama"
print(names1)
print(names2)

names1 = ["naruto","sasuke","kakasi","hinata"]
names2 = names1.copy()

names2[0] = "madara"
print(names1)
print(names2)

names1[0] = "hasirama"
print(names1)
print(names2)

# 演算子でリストを結合する
names1 = ["東京","埼玉","神奈川","千葉"]
names2 = ["栃木","長野","大阪","福島"]
names3 = names1 + names2
print(names3)

# リストを結合(extend()メソッドを使う)
names1 = ["東京","埼玉","長野","神奈川"]
names2 = ["大阪","京都","静岡","熱海"]
names1.extend(names2)
print(names1)