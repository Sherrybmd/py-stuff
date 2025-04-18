
def fizzBuzz(n):
    answer = ""
    dic = {
        3 : "Fizz",
        5 : "Buzz"
    }
    for num in range(1,n+1):

        answer = ""
        for k,v in dic.items():
            if (num % k) == 0:
                answer += v
        print(answer or num)


fizzBuzz(1000000)

