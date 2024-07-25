class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Check odd-length palindromes
            single_center_palindrome = expandAroundCenter(i, i)
            if len(single_center_palindrome) > len(longest):
                longest = single_center_palindrome
            
            # Check even-length palindromes
            double_center_palindrome = expandAroundCenter(i, i + 1)
            if len(double_center_palindrome) > len(longest):
                longest = double_center_palindrome
        
        return longest
