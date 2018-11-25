"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

nums = []
def main():
    sum_ = 0
    for i in range(1, 101):
        sum_ += i

    squares_sum = 0
    for i in range(1, 101):
        squares_sum += i*i

    difference = sum_*sum_ - squares_sum
    print(difference)

if __name__ == "__main__":
    main()
