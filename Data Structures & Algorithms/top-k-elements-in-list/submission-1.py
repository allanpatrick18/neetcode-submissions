class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        sort_f = sorted(freq.values())
        sort_f = sort_f[-k:]
        res = []
        for ele in sort_f:
            for key, val in freq.items():
                if ele == val:
                    res.append(key)
                    del freq[key]
                    break
        
        return res

            