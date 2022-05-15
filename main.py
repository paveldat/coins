import math

def minCountOfCoints(N, coins):
    numbers, Coins = (N+1) * [0], (N+1) * [0]
    for i in range(1, N+1):
        numbers[i] = math.inf
        Coins[i] = -1
    for i in range(0, len(coins)):
        for j in range(1, N+1):
            if j >= int(coins[i]):
                if numbers[j-(int(coins[i]))] + 1 < numbers[j]:
                    numbers[j] = 1 + numbers[j-int(coins[i])]
                    Coins[j] = i
    printCoinCombination(Coins, coins)
    return numbers[N]

def printCoinCombination(Coins, coins):
    coinsRes = {coin:0 for coin in coins}
    start = len(Coins) - 1
    while start != 0:
        j = Coins[start]
        coinsRes[coins[j]] += 1
        start -= int(coins[j])
    for coin in coins:
        print(f"Coin {coin} used {coinsRes[coin]} times")

def main():
    N = int(input("Enter the number: "))
    coins = list(input("Enter the list of available coins: ").split())
    print(f"Total numbers of coins: {minCountOfCoints(N, coins)}")

if __name__ == "__main__":
    main()