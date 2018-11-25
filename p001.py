"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    sum_ = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i

    print(sum_)
if __name__ == "__main__":
    main()
