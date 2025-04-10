def myfunc(n):
    print("yo")
    return lambda a : a * n


giga = myfunc(2)

print(giga(2))
