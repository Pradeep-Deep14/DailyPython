def func(a,b=[]):
    b.append(a)
    return b

result1 = func(1)
print(result1)
result2 = func(2)
print(result2)