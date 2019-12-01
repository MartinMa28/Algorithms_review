# Algorithms_review
Implementations of common data structures and algorithms


## Nov.15 2019
Word Square: Hard backtracking, it's hard to determine the next valid candidate.  
Redundant Connection: Needs to return the first edge that makes the cycle. Use disjoint set to find the first pair of vertices that belong to the same set. However, topological sort using BFS + in-degree or DFS cannot find the first edge that makes the cycle.


## Nov.16 2019
Weekly contest 163
- Shift 2D Grid
- Find Elements in a Contaminated Binary Tree
- Greatest Sum Divisible by Three (Trying 2d DP TLE)

Cheapest Flights Within K Stops: (Single source shorest path with the limit of hops) Dijkstra algorithm


## Nov.17 2019
Valid Palindrome: check if the alphanumeric characters in a string form a palindrome.  
Valid Palindrome 2: two pointer squeeze to the middle. Greedy algorithm, only allows inequality once.  
Review merge sort & quick sort


## Nov.18 2019
Fixed the bug in quick sort. When swapping values in-place, don't use slicing. Use the index instead.  
Kind of knowing how to implement Tarjan algorithm to find all of articulation points.  
Coin Exchange 2: Unbounded knapsack problem  
Remove Invalid Parentheses: BFS with 2 queues find all of candidates level be level  
Kth Smallest Element in a Sorted Matrix: Using binary search or min heap  


## Nov.19 2019
Basic Calculator II: Use a queue to evaluate an expression, which doesn't contain parentheses.  
Basic Calculator: Use a stackt to evaluate an expression, which does have parentheses, but only has plus and minus operators.  
Integer Break & Rod Cut: Similar to unbounded knapsack problem, 1 dimensional dynamic programming.  
Cut Ribbon: Find the proper length of the ribbon using binary search.  
All Nodes Distance K in Binary Tree: Convert a binary tree (acyclic connected directed graph) to an undirected graph. And then find the nodes using BFS.  

### TBD
Word Ladder (Done)  
Binary Tree Maximum Path Sum (Done)


## Nov.20 2019
Word Ladder: BFS find the shortest path (the minimum number of hops). Create masks for each word to build the graph.  
Binary Tree Maximum Path Sum: Find the path using bottom up traversal. Always update the maximum sum variable.  
Count Univalue Subtrees: Bottom up traversal.  
Unique Binary Search Trees: Dynamic programming. Given the number of nodes, count the number of unique BST. BST is used to reduce different permutation of nodes.  
3 Sum: Multiple 2-Sum & two pointers  
Binary Search Tree Iterator: inorder traverse the BST.  

### TBD
Distribute Coins in Binary Tree (Done)  
3 Sum Closest  (Done)
Iterative inorder traversal  (Done)  
Paint House II O(nk) O(nk^2) right now  
Longest Valid Parentheses  
House Robber II  

More binary search  
More sliding window  (Done)

## Nov.21 2019 
Distribute Coins in Binary Tree: Use DFS to count the balance value recursively for each sub-tree.  
3 Sum Closest: two pointers, squeeze to the center, update the closest sum.  
Binary Search Tree Iterator: simulate the iterative way to do the in-order traversal.  
Paint House: basic 2 dimensional dynamic programming (top down & bottom up), fixed amount of colors  
Paint House 2: 2 dimensional dynamic programming, runtime could be optimized to O(nk).  
Minimum Window Substring: dynamic sliding window (the size of it is changing)  
Minimum Size Subarray Sum: dynamic slidng window again  
Subsets: backtracking through the DFS, push every subset into the result.  
Subsets II: to get rid of duplicated subsets, sort the nums before backtracking. Don't traverse the same value during the DFS.  
Combinations: backtracking  
Combination Sum: backtracking  
Permutations: backtracking  
Permutations 2: backtracking  

## Nov.22 2019
Practice more binary search questions.
Refresh the meaning of left <= right, left < right and left + 1 < right  

## Nov.23 2019
Find Kth smallest pair distance: Find the Kth smallest pair using binary search. Use two pointer to count the number of smaller pairs in a sorted list.  
Course Schedule: Use DFS detect if there is a cycle in the directed graph.  
Course Schdule 2: Use BFS and in-degree to get the topological sort of the graph.  
Minimum Time Visiting All Points: Compute the moves needed between two points. And then add the number of moves together.  
Count Servers that Communicate: If at least two servers connected in a row or column, add those connected coordinates into a hash set. Return the number of elements in the hash set.  
Search Suggestions System: Use the startswith method in python, haven't tried trie.  
Number of Ways to Stay in the Same Place After Some Steps: top-down DP, the sub-problem is to find how many ways we could move from current index to the 0 position using a certain amount of steps.  
More binary tree questions regarding recursion.  

### TBD
House Robber III (Done) 
Split BST  (Done)
More substring, subsequence DP  
Trie  
Prepare for the resume  

## Nov.29 2019
Sliding window maximum: maintain a monotonic queue using double ended queue, kick out smaller elements when enqueuing new elements  
Sliding Puzzle: BFS + hash set + deepcopy when using composite object  
Word Break: DFS + memoization  
Maximum Product Subarray: strange DP, need to review  
Maximal Square: DFS + memo (super slow), DP fixes each position as the bottom right corner, so only needs to check 3 direction  
LRU Cache: hash table helps fast look ups, double linked list helps fast removals  

### TBD
Word Break II  
More subarray, subsequence DP  
Pratice runtime analysis  


## Nov.30 2019
Weekly contest 165:
- Find winner on a tic tac toe: simulation problem  
- Number of Burgers with No Waste of Ingredients: linear equation of two unknown  
- Count Square Submatrices with All Ones: Similar to Maximal Square (221)  

Reverse Linked List: recursively put current node at the end of the reversed the rest of nodes  
Minimum Height Trees: Trim leaves. After trimming each leaf, check if deleting it creates a new leaf. If so, put the new leaf in another queue. In this way, we could avoid traversing all of nodes in a tree.  