# username = 'aviralanddivya'

# def func():
#     # username = 'chai'
#     print(username)

# print(username)
# func()

# x = 95

# def func2(y):
#     z = x + y
#     return z

# res = func2(1)
# print(res)

# x = 99

# def func3():
#     global x
#     x = 12
#     print(x)

# func3()
# print(x)
# x = 99
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()

x = 99

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(2))