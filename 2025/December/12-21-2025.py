"""
A teacher must divide a class of students into two teams to play dodgeball. 
Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.
Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.
students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

On the other hand, given the input below, you should return False.
students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
"""

from collections import deque

def split_teams(students):
    color = {}  # student -> 0 or 1

    for student in students:
        if student not in color:
            # start BFS from this student
            queue = deque([student])
            color[student] = 0

            while queue:
                u = queue.popleft()
                for v in students[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False

    team_a = {s for s in color if color[s] == 0}
    team_b = {s for s in color if color[s] == 1}
    return team_a, team_b


"""
Keep a dictionary color:
0 → Team A
1 → Team B

For each student (important: graph may be disconnected):
    If not colored yet, start BFS/DFS and assign them a color.

For every enemy edge (u, v):
    If v is uncolored → assign opposite color of u
    If v already has same color as u → impossible, return False
    If no conflicts occur → return the two teams.
"""