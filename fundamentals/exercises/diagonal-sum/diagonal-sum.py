# fails under certain circumstances, maybe a funky input?
def diag(arr):

    def start(direction=1):

        sum = 0
        if direction == 1:
            row = 0
            column = 0
        else:
            direction = -1
            row = arr.index(arr[-1])
            column = 0

        while row < len(arr) and column < len(arr) and column >= 0 and row >= 0:

            sum += arr[row][column]

            row += direction
            column += 1

        return sum
    res = start(1) - start(-1)
    print(abs(res))
    return abs(start(1) - start(-1))

arr2 = [[1,2,3],[4,5,6,],[7,8,9]]
arr = [[11,2,4],[4,5,6],[10,8,-12]]
diag(arr)


