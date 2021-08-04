import numpy as np


# Checking if the number is prime.

def checkprime(n):
    if n == 1:
        print("1 is neither prime nor composite.")
    elif n == 2:
        print("2 is a prime number.")
    elif n >= 3:
        for i in range(2,n):
            if (n%i)==0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
    

    
# Finding out primes in a range and no. of primes.
        
def prime(l,u):
    p = []
    for i in range(l,u+1):
        if i == 1:
            continue
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            p.append(i)
    print(p)
    print(f"\nThere are {len(p)} prime numbers between {l} and {u}")

# nth prime number
    
def nth_prime(n):
    p = [2]  # first prime number
    num = 3  # start from 3
    while len(p) <= n:  # to calculate primes upto required count
        for i in p:
            if num%i==0:
                break
        else:
            p.append(num)
        num+=2  # skip even numbers
    print(f"The {n}th prime number is {p[-2]}")  # as python as 0 indexing returning second last element. 

# nth_prime(10) will return 11th prime number if we return the last element because of 0 indexing.
# counting starts from zero.