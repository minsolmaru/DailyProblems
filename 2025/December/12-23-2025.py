"""
You have N stones in a row, and would like to create from them a pyramid.
This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one.
In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary. 
Given this information, determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].

"""
def min_cost_pyramid(A):
    n = len(A)
    
    left = [0] * n
    right = [0] * n
    
    # Left to right
    left[0] = 1
    for i in range(1, n):
        left[i] = min(A[i], left[i-1] + 1)
    
    # Right to left
    right[-1] = 1
    for i in range(n-2, -1, -1):
        right[i] = min(A[i], right[i+1] + 1)
    
    # Final shape & cost
    cost = 0
    for i in range(n):
        final_height = min(left[i], right[i])
        cost += A[i] - final_height # this will be 0 if no change. k if k change.
    
    return cost


"""
greedy algorithm for optimal pyramid left to right and right to left under assumption 
- height only increases by one until max height in which height only decreases by 1
- cost of 1 to make optimal pyramid work


then combine the minimum of both left and right greedy pyramid. 
this works as we have constructed the left and right to be that way
we also take the minimum to minimise cost. MAX would break the pyramid and anything less than the min of the two would increase costs.
we also take one final cost at the end if there are duplicates. 

"""