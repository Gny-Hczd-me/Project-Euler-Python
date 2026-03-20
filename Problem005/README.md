# Problem 005 - Smallest Multiple

Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

## Solution Approach
- Start with 20! (factorial of 20) as an initial multiple
- Divide by prime numbers (2, 3, 5, 7, 11, 13, 17, 19) as long as the result is still divisible by all numbers from 2 to 20
- This reduces the factorial to the smallest number that is divisible by 1 through 20

## Result
232792560