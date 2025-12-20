"""
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.
Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:


        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |

"""

def min_quxes(line):
    r = line.count('R')
    g = line.count('G')
    b = line.count('B')
    n = len(line)

    # If only one color present, no transformations possible
    nonzero = sum(c > 0 for c in (r, g, b))
    if nonzero <= 1:
        return n

    # Otherwise, answer is 2 iff all parities match; else 1
    if (r % 2) == (g % 2) == (b % 2):
        return 2
    return 1
print(min_quxes(['R', 'G', 'B', 'G', 'B']))
print(min_quxes(['R''R','R','R','R',] ))