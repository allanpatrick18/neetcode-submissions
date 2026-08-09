class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freq1 = {}
        freq2 = {}

        for i in range(0, len(s1)):
           freq2[s2[i]] = 1 + freq2.get(s2[i], 0)
           freq1[s1[i]] = 1 + freq1.get(s1[i], 0)

        l =  0
        size = len(s2)
        size1 = len(s1)
        eq = True
        for k, v in freq1.items():
            if k in freq2:
                if freq2[k] != v:
                    eq = False
                    break
            else:
                eq = False
                break
        if eq:
            return True
            
        for r in range(len(s1),size):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            print(l,r, s2[l], s2[r])
            if s2[l] in freq2 and freq2[s2[l]] > 1:
                freq2[s2[l]] -= 1
            else:
                del freq2[s2[l]]
            print(freq2)
            print(freq1)
            
            eq = True
            for k, v in freq1.items():
                if k in freq2:
                    if freq2[k] != v:
                        print(k,v)
                        eq = False
                        break
                else:
                    print(k,v)
                    print(freq2)
                    eq = False
                    break
            
            if eq:
                return True
                   
            l = l + 1
        
        return False
            