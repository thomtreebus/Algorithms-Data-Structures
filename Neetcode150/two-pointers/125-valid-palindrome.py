class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1 
            hi -= 1
        return True