# 演算子
a = 13
b = 5
print(a % b)
print(a // b)

# 代入演算子
"""
=	a = 2	a = 2
+=	a += 2	a = a + 2
-=	a -= 2	a = a - 2
*=	a *= 2	a = a * 2
/=	a /= 2	a = a / 2
%=	a %= 2	a = a % 2
//=	a //= 2	a = a // 2
**=	a **= 2	a = a ** 2
"""
a = 2
a *= 3
print(a)

# 論理演算子
a = 2
b = 2
print(a == b and a < 5)

a = 6
b = 6
print(a == b and a < 5)
"""
and	a == b and a < 5	両方 True の時のみ True を返す
or	a == b or a < 5	片方が True であれば True を返す
not	not(a == b)	引数（括弧の中）が True であれば False、
False であれば True を返す
"""
