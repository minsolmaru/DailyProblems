"""
The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:
4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.

"""


def kaprekar_constant(n:int) -> int:
    if not (0 <= n <= 9999):
        raise ValueError("Number must be between 0 and 9999 inclusive.")
    
    s = f"{n:04d}"
    if len(set(s)) < 2:
        raise ValueError ("n must have at least 2 distinct digits")
    
    target = 6174
    steps = 0 

    while n != target:
        s = f"{n:04d}"
        asc = int("".join(sorted(s)))
        desc = int("".join(sorted(s, reverse = True)))
        n = asc - desc
        steps += 1
    

    return steps


print(kaprekar_constant(1234))