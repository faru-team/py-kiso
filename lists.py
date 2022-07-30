# リスト(list)-配列について
# 例: names = ["Sakura", "Tunade", "Hinata"]
names = ["Sakura", "Tunade", "Hinata"]
print(names[0])
print(names[2])

names = ["Sakura", "Tunade", "Hinata"]
print(names[-1])
print(names[-2])

names = ["Sakura", "Tunade", "Hinata"]
print(names)

names[1] = "Hanabi"
print(names)

# append()メソッドでリストに要素を追加する
names = []
names.append("Sakura")
print(names)

names.append("Tunade")
print(names)

names.append("Hinata")
print(names)

# insert()メソッドでリストに要素を追加
names = ["Sakura", "Tunade", "Hinata"]
print(names)

names.insert(1, "Hanabi")
print(names)

# 範囲指定した要素持つ新しいリストを取得する
names = ["Sakura","Sasuke","Naruto","Kakasi"]
print(names[1:4])
print(names[:3])
print(names[1:])
