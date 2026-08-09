class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ m for m in s if m.isalnum()]
        print(s)
        size = len(s)
        for i in range(0, size):
            if s[i].lower() != s[size -i-1].lower():
                return False
        return True
