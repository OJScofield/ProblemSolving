import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 1:
            median = float(nums1[len(nums1) // 2])
            return median
        else:
            median = float((nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2)
            return median