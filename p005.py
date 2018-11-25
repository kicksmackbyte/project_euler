"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

nums = []
def poo(x):
    for n in nums:
        if x % n == 0:
            x /= n

    nums.append(x)
    return x

def main():
    num = 1
    for n in range(1, 21):
        num *= poo(n)

    print(num)

if __name__ == "__main__":
    main()
