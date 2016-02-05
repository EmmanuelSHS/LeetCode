# LeetCode
The folder containing not only leetcode questions for algorithms & database, but also the other classic algorithms from other open judges.

### DP
LINT_longest_com_subseq.cpp:
    
    Given two strings, find the longest common subsequence.

    LCS is defined as https://en.wikipedia.org/wiki/Longest_common_subsequence_problem.
OTHER_Min_Imbalance.cpp:

    Given an input of array a and a partition k, we split a[n] into k+1 subarray. 
    Also, let an Imbalance of Array defined as the largest distance from the sum of any
    subarray to the average of subarray (sum(a[n])/(k+1)).

    Output: a number of the Imbalance of Array s.t. its the smallest among all
    possible partitions given a[n] & k.


LINT_Backpack.cpp:

    Given n items with size A_{i}, an integer m denotes the size of a backpack. How full you can fill this backpack? 
    You function should return the max size we can fill in the given backpack. 
    O(n x m) time and O(m) memory. 
    O(n x m) memory is also acceptable if you do not know how to optimize memory.

LINT_Coins_in_line.cpp:

    There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

    Could you please decide the first play will win or lose?

    O(n) time and O(1) memory.  

LINT_EditDistance.cpp:

    Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

    You have the following 3 operations permitted on a word:

        Insert a character

        Delete a character

        Replace a character

LINT_longest_incre_subseq.cpp:
	
	Given two strings, find the longest common subsequence (LCS). Your code should return the length of LCS.
	
LINT_word_break.cpp:

	Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

lint_unique_path.py:

    Return unique paths from left-upper-most corner to right-down-most corner. You may suppose that one can only travel right down.

lint_jump_game.py:

    Given a list A of max steps A[i] that you could jump from the i-th position. Return whether one could start from i = 0 and jumped to i = len(A) - 1.

lint_minPatSum.py:

    Given a m*n non-negative array, return the min sum of the path from left-up most to right-down most.

lint_numTree.py:

    Given a number n, find number of unique BST(binary search tree). More eg on http://www.lintcode.com/en/problem/unique-binary-search-trees/

lint_house_robber.py:

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police. Note that money couldn't be stolen from adjacent houses.

lint_distinct_subsequence.py:

	Given a string S and a string T, count the number of distinct subsequences of T in S.
	
lint_longest_common_substring.py:

	Given two strings, find the longest common substring. Return the length of it. Note that substring should be one in continuous manner.
	
	
lint_max_product_subarray.py:

	Find the contiguous subarray within an array (containing at least one number) which has the largest product.
	
	
        
### Bit Manipulation
LEET_Single_Number:

	Given an array of integers, every element appears twice except for one. Find that single one.

LINT_aplusb.cpp:

	Give two 32-bit int, adding w/o using "+" operand.

### Greedy
LEET_stock_sell_buy_II.cpp:

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
	
lint_gas_station.py:

	There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

	You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

	Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
	
lint_majority_number_ii.py:

	Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array. Provide with a O(n) running time & O(1) space algorithm.


### Hashing
LINT_2_sum.cpp:

	Given an array of integers, find two numbers such that they add up to a specific target number.

lint_anagrams.py:

	Given an array of strings, return all groups of strings that are anagrams.

### Recurrence
lint_generate_parentheses.py:

	Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
	
lint_graphic_valid_tree.py:

	Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
	
### Data Structure
lint_implement_trie.py:

	Implement a trie with insert, search, and startsWith methods.
	
### Sorting
lint_median.py:

	return the median of input array in O(n) time.
	
lint_kth_largest_element.py:

	return the k-th largest elements of input array, O(n) running time, O(1) extra space.
	
lint_3sum.py:

	return distinct sets of 3 elements (ascending order) for input array. O(n^2) runtime.

lint_largest_number.py:

    return a string of number that is the largest possible composed by given input array. O(nlog(n)) runtime.

lint_partitionArray.py:

    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

        All elements < k are moved to the left
        All elements >= k are moved to the right
        Return the partitioning index, i.e the first index i nums[i] >= k.

    if all number smaller than k, return len(nums)

lint_sort_colors.py:

    Iterate once to sort all the 0s 1s & 2s.

lint_sort_colors_ii.py:

    Altogether k colors, pls sort w/o counting sort.

lint_sort_by_case.py:

    Sort a string by lower cases first and upper cases later. In-place & O(n) (one-pass).

lint_max_gap.py:

    Return the max diff between two neighboring numbers in sorted array. O(n) time & space.


