n = 1260
numChanges = 0

coins = [500, 100, 50, 10]

for coin in coins:
    numChanges += n // coin
    n %= coin
    
print(numChanges)

