from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        
        # Merge the two arrays
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1
        while i < m:
            merged.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        # Find the median
        total_len = m + n
        if total_len % 2 == 0:
            mid1 = total_len // 2 - 1
            mid2 = total_len // 2
            return (merged[mid1] + merged[mid2]) / 2
        else:
            mid = total_len // 2
            return merged[mid]
