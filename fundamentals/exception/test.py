class A(Exception):
    print("there was tomfoolery HAPPENING")

class B(A):
    pass

class C(B):
    pass

for cls in [C,B,A]:
    try:
        raise cls()
    except C:
        print("C")
    except B:
        print("B")
    except A:
        print("A")
