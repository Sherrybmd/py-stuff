import time



# good buzz 0.009864568710327148  sec
# bad  buzz 0.01142573356628418   sec
# 16% less efficient

def fizzBuzz(choice):

    start = time.time()

    for number in range(1, choice):

        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")

        elif number % 3 == 0:
            print("fizz")

        elif number % 5 == 0:
            print("buzz")

        else:
            print(number)

    end = time.time()
    taken = end - start
    print(taken)

fizzBuzz(1000)








