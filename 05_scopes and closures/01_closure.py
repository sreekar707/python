# username="chaiaurcode"
# def func():
#     username="chai"
#     print(username)
    
# print(username)
# func() 


# x=99
# def func2(y):
#     z = x + y
#     return z

# result=func2(1)
# print(result)

def chaicoder(num):
    def actual (x):
        return x ** num
    return actual

f=chaicoder(3)
# g=chaicoder(3)

print(f(2))
# print(g(3))