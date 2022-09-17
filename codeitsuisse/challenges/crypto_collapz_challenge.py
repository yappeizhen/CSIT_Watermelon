
# Base case:
# if the current price is 1 --> 1*3+1 = 4 / 2 / 2 == 1 --> i.e. max price is 4
# if the current price is 2 --> 2 / 2 = 1 --> max price is 4
# if the current price is 3 --> 3*3+1 = 9*3+1 = 28/2 = 24/2 = 12/2 = 6/2 = 3 --> max is 28

def stream_crypto_collapz(data: list):
    res = []
    for input in data:
        res.append(crypto_collapz(input))
    return res

def crypto_collapz(input:list):
    res = []
    map = {1: 4}
    for item in input:
        res.append(findMax(item, map))
    return res

def findMax(num:int, map:dict):
    # Memoise past max values
    if num in map:
        return map[num]
    map[num] = num
    cur = num    
    while True:
        if isOdd(cur):
            cur = cur * 3 + 1
            map[num] = max(map[num], cur)   # Update local max value
        else:
            cur /= 2
        if cur in map:
            map[num] = max(map[num], map[cur])  # Check if local max > potential max
            break
        if cur == num:
            break
    return int(map[num])

def isOdd(item:int):
    return item % 2 != 0