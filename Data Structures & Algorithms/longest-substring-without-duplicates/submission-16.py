class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        sub = set()
        # subM = 1 if len(s) == 1 else 0
        # while r < len(s):
        #     sub.add(s[l])
        #     subM = max(subM, 1)
        #     if s[r] not in sub:
        #        sub.add(s[r])
        #        subM = max(subM, len(sub))
        #     else:
        #         sub = set()
        #         l = l + 1
        #         r = l
        #     r = r + 1

        # return subM
        res = 0
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l = l + 1

            sub.add(s[r])
            res = max(res,len(sub))
            r = r + 1
        
        return res
             