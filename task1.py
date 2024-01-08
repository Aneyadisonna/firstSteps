def arrangeCoins(num):
    step = 0
    coins = 0
    
    while num >= coins:
        step += 1
        coins += step

    return step - 1


print(arrangeCoins(5))
print(arrangeCoins(8))
