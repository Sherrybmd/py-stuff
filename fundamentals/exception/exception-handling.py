# https://docs.python.org/3/tutorial/errors.html#exceptions

while True:
    try:
        x = int(input("Enter a number: "))
        break

    except ValueError:
        print("not a valid number. try again")

