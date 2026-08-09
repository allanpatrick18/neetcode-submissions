class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq = {}
        for ele in s1:
           freq[ele] = 1 + freq.get(ele, 0)
        freq1 = freq.copy()
        l =  0
        size = len(s2)
        size1 = len(s1)
        for r in range(size):
            while l < size and s2[l] in freq and freq[s2[l]] > 0:
                print(r,l,s2[l])
                freq[s2[l]] -= 1
                l = l + 1
                print(l - r,size)
                if l - r  == size1:
                    return True
            
            freq = freq1.copy()
            print(freq1)
            l = r + 1
        
        return False
            