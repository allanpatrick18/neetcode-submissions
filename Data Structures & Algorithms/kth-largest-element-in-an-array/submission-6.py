class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [ele * (-1) for ele in nums]
        heapq.heapify(maxHeap)
        res = 0
        while k > 0:
           res = heapq.heappop(maxHeap)
           k -= 1
        
        return res * (-1)