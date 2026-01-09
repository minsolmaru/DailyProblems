"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

"""



def get_row(k):
    row = [1] * (k + 1)
    
    for i in range(2, k + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    
    return row


