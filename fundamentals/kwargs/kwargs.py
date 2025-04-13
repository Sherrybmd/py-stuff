# **name = takes arguments as dictionary with key:value pairs
# typically used as: **kwargs, you can use any name though.

def hello(**name):

    print("Hello")
    for key, value in name.items():
        print(key, ":", value)

# key = first, value = "shahryar"
hello(first="shahryar", middle="nigga", last="bmd")
