# _____________________________________________________________________

mystring = "this is some text"

mynumber = 8

mybadnumber = "12"


userinput = input( "this will receive a string from user: " )

# use type casting to use input as number



# _____________________________________________________________________

if userinput.isascii():
    pass

else:
    userinput = int( userinput )


if type(userinput) == str:
    print("input is string!")

elif type(userinput) == int:
    print("input is int!")

else:
    print("not sure")

# _____________________________________________________________________

while True:

    mynumber += 1

    if input("stop? y/n > ") == 'y':
        break



