"""
A knight is placed on a given square on an 8 x 8 chessboard. 
It is then moved randomly several times, where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on.

After k moves, what is the probability that the knight remains on the board?
"""

def knight_probability(r, c, k):
    moves = [
        (2,1), (2,-1), (-2,1), (-2,-1),
        (1,2), (1,-2), (-1,2), (-1,-2)
    ]
    
    dp = [[0]*8 for _ in range(8)]
    dp[r][c] = 1.0

    for _ in range(k):
        new_dp = [[0]*8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if dp[i][j] > 0:
                    for dx, dy in moves:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < 8 and 0 <= nj < 8:
                            new_dp[ni][nj] += dp[i][j] / 8
        dp = new_dp

    return sum(map(sum, dp))
