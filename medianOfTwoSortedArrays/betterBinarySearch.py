from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Partition the smaller array
            partitionA = (left + right) // 2
            # Partition the larger array based on partitionA
            partitionB = (m + n + 1) // 2 - partitionA

            # Handle edge cases for the partitions
            maxLeftA = float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float("inf") if partitionA == m else nums1[partitionA]
            maxLeftB = float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float("inf") if partitionB == n else nums2[partitionB]

            # Check if we have found the correct partitions
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # If total length is even, median is the average of the two middle values
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    # If total length is odd, median is the max of the left half
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                # Move towards the left in nums1
                right = partitionA - 1
            else:
                # Move towards the right in nums1
                left = partitionA + 1
