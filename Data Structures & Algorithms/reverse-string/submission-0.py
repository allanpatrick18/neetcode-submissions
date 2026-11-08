class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[size - 1 - i]
            s[size - 1 - i] = tmp
        return