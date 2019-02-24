"""

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def is_triplet(a, b, c):
    return (a**2 + b**2 == c**2)


def main():
    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(1, 500):
                if (a + b + c) == 1000:
                    if is_triplet(a, b, c):
                        print(a*b*c)
                        return

if __name__ == "__main__":
    main()
