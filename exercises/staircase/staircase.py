def staircase(n):

    for i in range(1, n+1):
        print(" " * (n-i) + ("#" * i))

# main
n = int(input("enter rows:\n>"))


staircase(n)
