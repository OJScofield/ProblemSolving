# Problem
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

[Problem Link](https://leetcode.com/problems/two-sum/)

# Solution
This problem was solved in three ways:

1- Brute Force: Iterating over the array/list using two for loops and checking to see if any two numbers' sum match the target. The time complexity is O(n^2) and the space complexity is O(1)

2- Two Pass Hashmap: A hashmap was used as a more efficient solution, where the values of the numbers in the array/list represented the keys in the hashmap and the indices of the numbers in the array/list represented the values in the hashmap. The first pass inserts the keys & values into the hashmap and the second pass checks to see if any value's complement is in the hashmap and returns the indices of these two values if found, while making sure the complement is not the same as the value itself. The time complexity is O(n) and the space complexity is O(n).

3- One Pass Hashmap: An even better soluton was to check to see if the current value in the array's complement is in the hashmap before inserting the value into the hashmap, and returning the indices of the value and its complement in case a solution is found, and this reduces the number of passes from two to one. The time complexity is O(n) and the space complexity is O(n).
