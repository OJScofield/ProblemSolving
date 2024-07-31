class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(i, j):
            left, right = i, j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if is_palindrome(start, start + length):
                    return s[start:start + length]
        
        return ""
