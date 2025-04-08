# i'd like to do this in c++
def miniMaxSum(arr):

    arr.sort()
    min = sum(arr[0:4])
    max = sum(arr[1:5])

    print(f"{min} {max}")
arr = [1,2,3,4,5]

miniMaxSum(arr)
