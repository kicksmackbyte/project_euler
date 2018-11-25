"""
What is the largest prime factor of the number 600851475143 ?
"""

import math

NUM = 600851475143
upper = math.ceil(math.sqrt(NUM))

primes = []
def is_prime(x):
    if x in primes:
        return True

    for p in primes:
        if x % p == 0:
            return False

    primes.append(x)
    return True

def main():
    largest_prime = 2

    for x in range(2, upper):
        if NUM % x == 0 and is_prime(x):
            largest_prime = x


    print(largest_prime)

if __name__ == "__main__":
    main()
