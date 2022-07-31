# dictionary - キーと値のペアの削除
dic = {
    "name" : "ナルト",
    "age"  : 18,
    "自己紹介": "主人公、忍び世界に9人しかいない特別な忍び"
}
# del文で辞書からキーと値のペアを削除
del dic["自己紹介"]
print(dic)

# エラーになる
"""dic1 = {
    "name" : "FaL",
    "age"  : 28,
    "自己紹介" : "よろ〜"
}
del dic1
print(dic1)
"""
# pop()メソッド使って、キーと値のペアを削除
dic.pop("age")
print(dic)

# popitem()メソッドで辞書からキーと値のペアを削除
# popitem()メソッドを使うと、最後に追加したキーと値のペアを削除
dic2 = {
    "name" : "うちはサスケ",
    "age"  : 18,
    "得意"  : "火遁",
    "自己紹介" : "うちは一族生残り、恨みを兄抱きながら少年時代を過ごしてきた"
}
dic2.popitem()
print(dic2)

# clear()メソッド使って、辞書からキーと値を全て削除
dic2.clear()
print(dic2)
