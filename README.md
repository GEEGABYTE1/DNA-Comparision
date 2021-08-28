# DNA Comparision Algorithm 🧬

This algorithm compares the order of nucleotides of two DNA strands and returns the common subsequence. This algorithm is great to compare and find out similarities between two types of DNA. 

For this algorithm, letters don't need to be directly next to each other. The comparision has been made broader for a general sequence. Take for example, `ACCGTT` and `CCAGCA`. The common subsequence would be `CCG`.

# Solution 🔮

The naive approach would be to split the string into small subsequences and compare them. However, this approach would have exponential time of `O(2^n)`. 

However, with dynamic programming, and the implementation of a matrix by comparing each row (letter) with each column per row (the rest of the letters in string 2), we can compare the letters directly, in a more efficient time of O(`len of string_1 * len of string_2)`. 

Note that for the time complexity, we don't take into consideration the formatting part (annotated in the script) as that is just extra. If we were to take that out and just return the desired result, the time complexity remains optimized.

# More Information
There are many different ways to optimize this algorithm, however, just for the purposes of dynamic programming, and it's practice, the algorithm is made this way.

You can also try different strings and compare them. In the script, they have been annotated, hence, under `Test Inputs` is where you can change the cases. However, the function does only compare two strings at a time. 

Made in Python 🐍
