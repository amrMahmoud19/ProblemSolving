def isPrime(num):
    
    for i in range(2,num):

        if num%i == 0:
            return False
        
    
    
    return True


def isPalin(num):

    n = str(num)

    itr = len(n)//2

    for i in range (itr):

        if n[i] != n[len(n)-i-1]:
            return False
    
    return True


def isPrimePalin(order):

    con = True
    num = 2
    rank=0
    while rank!=order:

        if(isPrime(num) and isPalin(num)):
            rank = rank +1

        num = num+1

    return num-1
# num = 1222
# print(isPalin(num))
order = 6
num = isPrimePalin(order)
print (num)