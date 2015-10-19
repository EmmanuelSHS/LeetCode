# LeetCode
The folder containing not only leetcode questions for algorithms & database.

But also the other classic algorithms.


LEET_Bit_Single_Number:

Given an array of integers, every element appears twice except for one. Find that single one.


LINT_DP_longest_com_subseq.cpp:
    
    Given two strings, find the longest common subsequence.

    LCS is defined as https://en.wikipedia.org/wiki/Longest_common_subsequence_problem.


OTHER_DP_Min_Imbalance.cpp:

    Given an input of array a and a partition k, we split a[n] into k+1 subarray. 
    Also, let an Imbalance of Array defined as the largest distance from the sum of any
    subarray to the average of subarray (sum(a[n])/(k+1)).

    Output: a number of the Imbalance of Array s.t. its the smallest among all
    possible partitions given a[n] & k.


LINT_DP_Backpack.cpp:

    Given n items with size A_{i}, an integer m denotes the size of a backpack. How full you can fill this backpack? 
    You function should return the max size we can fill in the given backpack. 
    O(n x m) time and O(m) memory. 
    O(n x m) memory is also acceptable if you do not know how to optimize memory.


LINT_DP_Coins_in_line.cpp:

    There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

    Could you please decide the first play will win or lose?

    O(n) time and O(1) memory.  

LINT_DP_EditDistance:

    Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

        Insert a character

        Delete a character

        Replace a character



