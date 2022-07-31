# if文では、条件式がTrueの時に指定した、コードブロックを実行する
"""
if [条件式A]:
    [コードブロックA]
elif [条件式B]
    [コードブロックB]
elif [条件式C]
    [コードブロックC]
else:
    [コードブロックD]
"""

a = 4

if a == 5:
    print("aは5です。")
elif a != 4:
    print("aは4ではありません。")
elif a > 2:
    print("aは2より大きいです。")
else:
    print("上の条件どれにも当てはまりません。")

# 複数の条件式
# andとor演算子を使って、複数の条件式を合わせる
# Trueの時の実行例
a = 7

if a != 4 and a > 6:
    print("aは4ではなくて、6より大きいです。")
else:
    print("aは4か、6以下です。")
# Falseの時の実行例
a = 5

if a != 4 and a > 6:
    print("aは4ではなくて、6より大きいです。")
else:
    print("aは4か、6以下です。")

# リスト(list)に値が含まれているか
names = ["A","B","C","D"]

if "A" in names:
    print("Aはリストに存在します。")
else:
    print("Aはリストに存在しません。")

if "x" in names:
    print("xはリストに存在します。")
else:
    print("xはリストに存在しません。")

# 辞書(dicionary)にキー(key)が存在するか
# pegeというオブジェクトの中にキーが存在するかを確かめるコード
pege = {
    "name": "a",
    "age" : 1,
    "gender": "b"
}

if "gender" in pege:
    print("genderというキーが存在します")
else:
    print("genderというキーが存在しません。")

