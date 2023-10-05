import math

def main():
    for i in range(5):
        print(f"{i} = {square(i)}")


def square(n):
    return n * n

def sqrt(n):
    math.sqrt(n)


if __name__ == "__main__":
    main()
