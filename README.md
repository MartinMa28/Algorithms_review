# Algorithms_review
Implementations of common data structures and algorithms

### Nov.15 2019
Word Square: Hard backtracking, it's hard to determine the next valid candidate.  
Redundant Connection: Needs to return the first edge that makes the cycle. Use disjoint set to find the first pair of vertices that belong to the same set. However, topological sort using BFS + in-degree or DFS cannot find the first edge that makes the cycle.

### Nov.16 2019
Weekly contest 163
- Shift 2D Grid
- Find Elements in a Contaminated Binary Tree
- Greatest Sum Divisible by Three (Trying 2d DP TLE)

Cheapest Flights Within K Stops: (Single source shorest path with the limit of hops) Dijkstra algorithm

### Nov.17 2019
Valid Palindrome: check if the alphanumeric characters in a string form a palindrome.  
Valid Palindrome 2: two pointer squeeze to the middle. Greedy algorithm, only allows inequality once.  
Review merge sort & quick sort
