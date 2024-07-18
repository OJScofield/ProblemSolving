# Problem
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

[Problem Link](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

# Solution
This solution merges two sorted arrays, sorts the combined array, and calculates the median with a time complexity of O((m+n)\log(m+n)) and a space complexity of O(1), while taking into consideration that the solution differs if the array length is even or odd.
