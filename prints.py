# 文字列について
# format()メソッド使い文字列をフォーマットする
name = "Sakura"
age = 28

message = "{}は{}歳.ピチピチの女性"
print(message.format(name, age))

name = "Sakura"
age = 28

message = "{0}は{1}歳.ピチピチの女性"
print(message.format(name, age))

name = "Sakura"
age = 28

message = "{{{0}}}は{1}歳.ピチピチの女性"
print(message.format(name, age))