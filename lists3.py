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