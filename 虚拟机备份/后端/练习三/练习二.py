class A(object):
    a = 1
    c = 5
    b = 6
    l = 10

a = A()
delattr(A,'c')
setattr(a ,'c',10)

print(a.c)





