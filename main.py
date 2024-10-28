"""A naive algorithm to find prime numbers in Python."""

import time
import sys


def find_all_primes(target):
    """Find all prime numbers smaller than or equal to target"""
    result = []

    if target <= 1:
        return result

    for value in range(2, target):
        for i in range(2, value):
            if value % i == 0:
                break
        else:
            result.append(value)

    return result


def runtime_calculator():
    target_values = [100, 500, 1000, 5000, 10000, 50000]

    for target in target_values:
        print(f"Testing {target}")

        start_time = time.time()
        prime_numbers = find_all_primes(target)
        duration = time.time() - start_time
        memory = sys.getsizeof(prime_numbers)

        print(f"Time usage: {duration:.10f} seconds")
        print(f"Memory usage: {memory} bytes")


if __name__ == "__main__":
    runtime_calculator()
