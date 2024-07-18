# Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Solution
This problem was solved in two ways, one solution where the digits are in reverse order (from LSB to MSB), and the other solution where the digits are in proper order (from MSB to LSB):

1- Reverse Order: The solution iteratively adds corresponding digits of two linked lists, handling carry-over values, and constructs the resulting linked list from least significant to most significant digit.

2- Proper Order: The solution reverses the input linked lists, iteratively adds corresponding digits while handling carry-over values, and then reverses the resulting linked list to represent the sum from the most significant to the least significant digit.
