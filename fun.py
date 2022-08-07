# user_function(ユーザ関数)について
def greet():
    print("Hello")

greet()

def fun(User, funUser):
    print(f"ユーザについて {User} {funUser}")

fun("あなたがユーザです", "ファル")
fun("あなたはユーザではありません", "違う人")

# ユーザの定義関数の引数をデフォルト値に指定する
def add(value1, value2, value3 = 0, value4 = 0):
    print(value1 + value2 + value3 + value4)

add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)

# 定義関数の可変長引数
# 引数が何個かわからないとき「 *　」を付ける
def add(*values):
    total = 0
    for v in values:
        total += v
    print(f"Total: {total}")

add(1, 2, 3)
add(1, 2, 3, 4, 5)

# 可変長のキーワード引数　「**」使う
def print_options(**options):
    for key, value in options.items():
        print(f"{key} = {value}")

print_options(option1 = 190, option2 = "test", option3 = True)
print("--------------")
print_options(opt1 = "test", opt2 = 2)