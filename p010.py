"""

Find the sum of all the primes below two million.

"""
import math

primes = [2, 3, 5, 7]
primes_sq = [4, 9, 25, 49]

def is_prime(num):
    if num in primes:
        return True

    for prime, prime_sq in zip(primes, primes_sq):
        if num % prime == 0:
            return False
        elif prime_sq > num:
            break

    primes.append(num)
    primes_sq.append(num**2)
    return True

def main():
    result = 0
    [is_prime(num) for num in range(2, 2000000)]

    for prime in primes:
        result += prime

    print(result)

if __name__ == "__main__":
    main()
