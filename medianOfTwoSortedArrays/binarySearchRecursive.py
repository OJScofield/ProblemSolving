from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Lengths of the two input arrays
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2

        # Helper function to find the k-th smallest element
        def find_kth(k, start1, end1, start2, end2):
            # If one array is exhausted, return the k-th element from the other array
            if start1 > end1:
                return nums2[start2 + k]
            if start2 > end2:
                return nums1[start1 + k]

            # Calculate the middle indexes and values of the current segments
            mid1 = (start1 + end1) // 2
            mid2 = (start2 + end2) // 2
            mid_val1, mid_val2 = nums1[mid1], nums2[mid2]

            # If k is larger than the sum of both middle indexes,
            # it means the k-th element is in the right halves of one of the arrays
            if (mid1 - start1) + (mid2 - start2) < k:
                if mid_val1 > mid_val2:
                    # Exclude the left half of nums2
                    return find_kth(k - (mid2 - start2 + 1), start1, end1, mid2 + 1, end2)
                else:
                    # Exclude the left half of nums1
                    return find_kth(k - (mid1 - start1 + 1), mid1 + 1, end1, start2, end2)
            else:
                if mid_val1 > mid_val2:
                    # Exclude the right half of nums1
                    return find_kth(k, start1, mid1 - 1, start2, end2)
                else:
                    # Exclude the right half of nums2
                    return find_kth(k, start1, end1, start2, mid2 - 1)

        # If the total length is odd, find the middle element
        if total_len % 2 == 1:
            return find_kth(total_len // 2, 0, len1 - 1, 0, len2 - 1)
        else:
            # If the total length is even, find the average of the two middle elements
            left_median = find_kth(total_len // 2 - 1, 0, len1 - 1, 0, len2 - 1)
            right_median = find_kth(total_len // 2, 0, len1 - 1, 0, len2 - 1)
            return (left_median + right_median) / 2
