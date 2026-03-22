#​ Problem 033 - Digit Cancelling Fractions
​Problem Statement
​Find the four non-trivial fractions (less than 1) where cancelling the common digit from the numerator and denominator gives the same value (e.g., 49/98 = 4/8).

##​ Solution Approach
​Range: Iterates through 2-digit numbers (10 to 99). 
​Non-trivial: Filters out multiples of 10 to avoid "trivial" solutions.
​Cancellation Logic: Checks if the last digit of the numerator (i) matches the first digit of the denominator (j).
​Verification: Validates if the simplified fraction (removing the common digit) is mathematically equal to the original fraction (i/j).

##​ Result
​The four fractions found are: 16/64, 19/95, 26/65, 49/98.