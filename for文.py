# for文 - inメソッド使ってやる
names = ["東京","埼玉","神奈川","長野"]

for name in names:
    print(name)

namex = ("香川","福井","新潟","高城")

for namex in namex:
    print(namex)

# 文字列の中一文字ずつ出力してみる
namex = "Tokyo"
for s in namex:
    print(s)

namex = "Saitama"
for x in namex:
    print(x)

# continue文を使う（continue文使ったブロック内はスキップされて実行されない)
names = ["東京","埼玉","神奈川","長野"]

for names in names:
    if names == "東京":
            continue
    print(names)

# break文を使ってfor文のループを抜けることができる
names = ["東京","埼玉","神奈川","長野"]

for names in names:
    if names == "東京":
        break
    print(names)

# for-else文、繰り返しが終わった後で else 文のコードブロックを一度だけ実行する
names = ["生徒A","生徒B","生徒C","生徒D","生徒E"]
for names in names:
    print(names)
else:
    print("どれも生徒Aには該当しません!")

# for文-range
"""
range の開始、終了の数字、ステップの指定の仕方は次の通りです。

range( 開始（整数）, 終了（整数）, ステップ（整数）)

終了だけが必須で、開始とステップはオプショナルで指定しなくても大丈夫
指定しないとデフォルトで開始は 0、ステップは 1 が使われる
"""

for i in range(4):
    print(i)

for s in range(2):
    print(s)

# for文-index (enumerate()関数を使うと、要素と共にindexが取得します)

names = ["生徒A","生徒B","生徒C","生徒D"]

for index, name in enumerate(names):
    print(index, name)

print("---------------------------------")
lists = ["武器A","武器B","武器C","武器D"]

for index, buki in enumerate(lists):
    print(index, buki)

names = ["武器0","武器1","武器2","武器3"]

for index in range(len(names)):
    print(index, names[index])


# for文-(辞書)dictionaryをループする
person = {
    "name": "武器A",
    "攻撃力": 20,
    "性能": "普通の武器Aです"
}

for key in person:
    print(key, person[key])

person = {
    "名前": "R武器",
    "攻撃力": 60,
    "性能": "武器Aよりは性能高い"
}

for key in person:
    print(key, person[key])

# 辞書のitems()メソッド使って、キーと値を取得する
person = {
    "名前": "SR武器",
    "攻撃力": 300,
    "性能": "武器AとR武器に比べるとかなりの性能が高い"
}

for key, value in person.items():
    print(key, value)

students = {
    "N武器": {
        "名前": "N武器",
        "攻撃力": 12,
        "レア度": "N",
        "性能": "弱"
    },
    "R武器": {
        "名前": "R武器",
        "攻撃力": 22,
        "レア度": "R",
        "性能": "弱上"
    },
    "SR武器": {
        "名前": "SR武器",
        "攻撃力": 60,
        "レア度": "SR",
        "性能" : "中"
    },
    "SSR武器": {
        "名前": "SSR武器",
        "攻撃力": 200,
        "レア度": "SSR",
        "性能": "最高"
    }
}

for student, student_info in students.items():
    print(student, student_info["名前"])

person = {
    "名前": "ファル",
    "年齢": 28,
    "趣味": "プログラミング"
}

for value in person.values():
    print(value)

# 応用編

ZicosyoKai = {
    "カテゴリ1": {
        "名前": "faru",
        "年齢": 28,
        "趣味": "アニメ" "プログラミング",
        "職業": "室内"
    },
    "カテゴリ2": {
        "名前": "ゆきだま",
        "年齢": 22,
        "趣味": "酒" "ヤニ",
        "職業": "料理"
    }
}

for ZicosyoKai, zicosyokai_info in ZicosyoKai.items():
    print(ZicosyoKai,zicosyokai_info["名前"])

kai = {
    "名前": "ファル",
    "年齢": 29,
    "趣味": "アニメ," "アプリゲーム," "プログラミング"
}

for Kai in kai.values():
    print(Kai)