# Uses python3
import sys

def get_change(m):
    coins=[1,3,4]
    num_coins =[0]
    use_coins =[0]
    for i in range(1,m+1):
        min_coin=10**6
        use_coin = 0
        for coin in coins:
            if coin <= i:
                if num_coins[i - coin] + 1 <= min_coin:
                    min_coin = num_coins[i - coin] + 1
                    use_coin = coin
                    #print(use_coin)
        num_coins.append(min_coin)
        use_coins.append(use_coin)
        #print(num_coins)
    return num_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
