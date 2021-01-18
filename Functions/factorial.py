import sys


def factorial(x):
    result = 1
    while x > 0:
        result = result*x
        x -= 1

    return result


if __name__ == "__main__":
    print(factorial(int(sys.argv[1])))
