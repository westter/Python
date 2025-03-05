class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        def isPalindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        longest = ""
        for i in range(len(s)):
            odd = isPalindrome(s,i,i)
            if len(odd) > len(longest):
                longest = odd
            even = isPalindrome(s,i,i+1)
            if len(even)>len(longest):
                longest = even
        return longest

s = Solution()
print(s.longestPalindrome("cbb"))
# returns bb
print(s.longestPalindrome("dumud"))
#returns dumud
