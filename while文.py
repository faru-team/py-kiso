# while文について
# インデントとコードブロック
"""
while [条件文]:
    [コードブロック]
"""



index = 0
while index < 5:
    # 演算子を使って1が足されていく
    index += 1
    print("index =", index)
    # 繰り返し実行されて、0-5まで出力される
# ここで繰り返す時に、ループを抜けるように、条件満たされた時の実行コード書く必要がある
lange = 10
while lange < 20:
    lange += 20
    print("lange =", lange)
    # ループ抜ける文を書いてないので永遠と実行しっぱなしになる
    # 修正してループ抜ける処理を書く

# while文でcontinueする
# continue文とは、コードブロック内のそれ以降のコードをスキップする
index = 0
while index < 5:
    index += 1
    if index == 2:
        continue
    print("index =", index)

# while文でbreakする
# breakとは、コードブロックの中で、while文を抜けることができます。
index = 0
while index < 5:
    index += 1
    if index == 4:
        break
    print("index =", index)
# while文 - else文する
# else文とは、条件文がFalseになった時
# else文のコードブロックを一度だけ実行する
index = 0
while index < 5:
    index += 1
    print("index =", index)
else:
    print("current index is", index)

values = 0
while values < 10:
    values += 1
    if values == 6:
        break
    print("values =", values)
else:
    print("no values is", values)