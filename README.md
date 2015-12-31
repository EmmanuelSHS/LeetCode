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

### Bit Manipulation
LEET_Single_Number:

	Given an array of integers, every element appears twice except for one. Find that single one.

LINT_aplusb.cpp:

	Give two 32-bit int, adding w/o using "+" operand.

### Greedy
LEET_stock_sell_buy_II.cpp:

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
	
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