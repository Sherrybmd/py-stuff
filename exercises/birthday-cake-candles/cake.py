def birthdayCakeCandles(candles):
    # Write your code here
    max = 0
    counter = 0

    for candle in candles:
        if candle > max:
            max = candle
            counter = 1

        elif candle == max :
            counter += 1

    return (counter)

arr = [3,2,1,3]
print(birthdayCakeCandles(arr))
