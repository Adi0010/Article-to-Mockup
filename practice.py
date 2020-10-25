class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s,t))