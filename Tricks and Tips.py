#/usr/bin/env python3.5
#Merging Two dictionary Values
di1={'a':1,'b':2}
di2={'c':1,'d':2}
di1.update(di2)
print(di1)

dic3 = {**di1,**di2}
print (dic3)

#Finding prime by SieveOfEratosthenes Algo

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print (p)

SieveOfEratosthenes(100)