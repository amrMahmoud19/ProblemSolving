def maximizeBig(n, m, x, y):
    if x<y:                    # in case a profit can be made from selling big candies, that's because we can sell big for more small and use 1 small to buy one big

        buy_m = n*y            # denoting buying small candies using available big candies
        n = 0                  # updating current no of big candies
        m += buy_m             # updating the no of small candies
    n+=(m//x)                  # buying big candies with amount of available small candies
    return n


n = 3
m = 10
x = 4
y = 2

print(maximizeBig(n,m,x,y))



    