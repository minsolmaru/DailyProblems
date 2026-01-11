"""
You are presented with an array representing a Boolean expression. The elements are of two kinds:

T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).
"""

def count_true_parenthesizations(expr):
    n = len(expr)
    
    # dp[i][j] = (true_count, false_count)
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

    # Base case
    for i in range(0, n, 2):
        if expr[i] == 'T':
            dp[i][i] = (1, 0)
        else:
            dp[i][i] = (0, 1)

    # Length of subexpression
    for length in range(3, n + 1, 2):
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            true_count = false_count = 0

            for k in range(i + 1, j, 2):
                op = expr[k]
                LT, LF = dp[i][k - 1]
                RT, RF = dp[k + 1][j]

                if op == '&':
                    true_count += LT * RT
                    false_count += LT*RF + LF*RT + LF*RF

                elif op == '|':
                    true_count += LT*RT + LT*RF + LF*RT
                    false_count += LF * RF

                elif op == '^':
                    true_count += LT*RF + LF*RT
                    false_count += LT*RT + LF*RF

            dp[i][j] = (true_count, false_count)

    return dp[0][n - 1][0]
