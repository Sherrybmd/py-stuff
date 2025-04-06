def plusMinus(arr):

    pos = neg = zer = 0
    max = len(arr)

    for num in arr:
        if num > 0:
            pos += 1

        elif num == 0:
            zer += 1

        elif num < 0:
            neg += 1

        else:
            error = "ERROR, cant read the array, enter numbers such as 1, 0, -1"
            print(error)

    posratio = pos/max
    negratio = neg/max
    zerratio = zer/max

    print(format(posratio, '.6f'))
    print(format(negratio, '.6f'))
    print(format(zerratio, '.6f'))

arr = [1,1,0,-1,-1]


plusMinus(arr)
