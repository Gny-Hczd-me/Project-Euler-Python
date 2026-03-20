# Problem 024 - Lexicographic Permutations

Find the millionth lexicographic permutation of the digits 0 to 9.

## Solution Approach
- Generate all permutations of digits from 0 to 9
- Store them in a list in lexicographic order
- Select the (10^6 - 1)th element (since indexing starts from 0)
- Convert the tuple of digits into a number

## Result
2783915460