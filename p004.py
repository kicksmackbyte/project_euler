"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(i):
    str_ = str(i)
    if str_ == str_[::-1]:
        return True
    else:
        return False

def main():
    num_1 = 999
    num_2 = 999

    palindromes = []

    for i in range(900):
        a = 999 - i
        for j in range(900):
            b = 999-j

            product = a * b
            if is_palindrome(product):
                palindromes.append(product)

    largest_palindrome = max(palindromes)
    print(largest_palindrome)

if __name__ == "__main__":
    main()
