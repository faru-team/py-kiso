# 辞書(dictionary)について
# 辞書とはキー(key)と値(value)の対した複数データの集まり
dic = {
    "name": "Naruto",
    "age" : 18,
    "gender" : "ナルトはアニメの主人公で人中力である"
}
dic1 = {
    "name" : "Sasuke",
    "age"  : 18,
    "gender": "うちは一族でナルト同期のライバル"
}
dic2 = {
    "name" : "Sakura",
    "age"  : 18,
    "gender": "一般家庭から忍びになったナルトと同期"
}
# nameというキーを取得するやり方は下に書いてる
print(dic1["name"])
print(dic2.get("name"))
# 辞書の値を変更する("gender")中身を変更
dic["gender"] = "ナルトは四代目火影の息子にして、平和をもたらす予言の子"
print(dic)
# キーと値のペアを追加する
dic["自己紹介"] = "ナルトという物語の主人公で、忍び世界9人しかいない特別な人"
print(dic) 