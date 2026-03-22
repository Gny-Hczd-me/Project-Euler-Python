# Project Euler #3: Largest Prime Factor

This script finds the largest prime factor of the number **600851475143**. It uses a brute-force trial division approach combined with a primality test to identify the maximum factor.

## How it Works
The algorithm follows these logical steps:

* **Iterative Search:** It starts from `num = 2` and increments by 1 in a `while` loop.
* **Primality Test:** For every `num`, it checks if the number is prime using the condition:
    `all(num % i != 0 for i in range(2, int(pow(num, 0.5)) + 1))`
* **Divisibility Check:** If `num` is prime, the script checks if it can divide the target number `a` without a remainder.
* **Reduction:** When a prime factor is found, it is stored in the **max** variable, and the target number is updated.
