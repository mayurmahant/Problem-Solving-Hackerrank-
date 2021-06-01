from statistics import mode
def birthdayCakeCandles(candles):
    sum=0
    for i in range(len(candles)):
        if candles[i] == max(candles):
            sum=sum+1
        
    return sum
