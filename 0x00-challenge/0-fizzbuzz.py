#!/usr/bin/python3
import sys

def fizzbuzz(n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz", end=" ")
            elif i % 3 == 0:
                print("Fizz", end=" ")
            elif i % 5 == 0:
                print("Buzz", end=" ")
        print()  # for a newline at the end
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("The argument should be an integer.")
        sys.exit(1)

    fizzbuzz(n)
