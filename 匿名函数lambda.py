def f(x):
    return x*x
print(list(map(f,range(1,10))))

print(list(map(lambda x: x*x,(range(1,10)))))