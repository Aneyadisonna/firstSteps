'''
Task 1
how many complete rows of coins (with increasing numbers of coins in each row) can be placed with a given number of coins `num`
'''


# first solution
def arrangeCoins(num):
    step = 0
    coins = 0
    
    while num >= coins:
        step += 1
        coins += step

    return step - 1


# second solution
def arrangeCoins2(num):
    return int(((8 * num + 1) ** 0.5 - 1) // 2)


print(arrangeCoins(5))
print(arrangeCoins(8))

print(arrangeCoins2(5))
print(arrangeCoins2(8))
