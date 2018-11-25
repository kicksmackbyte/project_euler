"""
What is the 10,001st prime number?
"""

primes = []
def is_prime(x):
    for p in primes:
        if x % p == 0:
            return False

    primes.append(x)
    return True


nums = []
def main():
    x = 2
    while(len(primes) < 10001):
        is_prime(x)
        x += 1

    print(primes[10000])

if __name__ == "__main__":
    main()
