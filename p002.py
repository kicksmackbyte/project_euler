"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

FIB_MEMO = [1, 1]
def fib(x):
    if x < len(FIB_MEMO):
        return FIB_MEMO[x]
    else:
        memo = FIB_MEMO[x-1] + FIB_MEMO[x-2]
        FIB_MEMO.append(memo)

        return memo

def main():
    x = 0
    sum_ = 0

    fib_ = fib(x)
    while(fib_ < 4000000):
        if fib_ % 2 == 0:
            sum_ += fib_

        x += 1
        fib_ = fib(x)

    print(sum_)

if __name__ == "__main__":
    main()
