# list - 要素の削除
naruto = ["Naruto","Sakura","Sasuke","Kakasi"]
print(naruto)

del naruto[1]
print(naruto)

# pop()メソッドでリストから要素を削除する
naruto = ["Naruto","Sakura","Sasuke","Kakasi"]
print(naruto)

# pop()メソッドで最後のリスト要素削除して、最後の要素を出力した
naruto_popped = naruto.pop()
print(naruto)
print(naruto_popped)

# pop()を使って、インデックスを指定して、要素を削除
naruto = ["naruto","sasuke","kakasi"]
print(naruto)

naruto.pop(1)
print(naruto)

naruto.pop(1) 
print(naruto)

# remove()メソッドでリストから要素を削除
naruto = ["naruto","sasuke","kakasi"]
print(naruto)

naruto.remove("naruto")
print(naruto)

naruto = ["naruto","sasuke","kakasi"]
print(naruto)

# clear()メソッドでリストから全要素を削除
naruto = ["naruto","sasuke","kakasi"]
print(naruto)

naruto.clear()
print(naruto)

# list-要素の並べ替える
# sort()メソッドでリストの要素を並べ替え
names = ["naruto","sasuke","kakasi"]
print(names)

names.sort()
print(names)

names = ["naruto","sasuke","kakasi"]
print(names)

names.sort(reverse=True)
print(names)

# 並び替え用の関数を指定してリストの要素を並び替える
names = ["Naruto","Sasuke","Kakasi"]
print(names)

names.sort()
print(names)

# sort()メソッドには、[key=関数]という形で並び替えに使う
names = ["Naruto","Sasuke","Kakasi"]
print(names)

names.sort(key=str.casefold)
print(names)

# sorted()関数で要素が並び替えらたリストを取得する
names = ["Naruto","Sasuke","Kakasi"]
names_sorted = sorted(names)

print(names)
print(names_sorted)

# reverse()メソッドで要素の並び順を反対にする
names = ["Naruto","Sasuke","Kakasi"]
print(names)

names.reverse()
print(names)
