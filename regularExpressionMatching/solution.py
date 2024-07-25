class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def check(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}

            if j + 1 < len(p) and p[j + 1] == '*':
                ans = check(i, j + 2) or (first_match and check(i + 1, j))
            else:
                ans = first_match and check(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return check(0, 0)
