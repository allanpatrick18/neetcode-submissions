class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
       # Solution 1 
       #  order and the list

    #    nums.sort()
    #    return nums[len(nums) - k]

       # Solution 2
       # maxheap
       maxHeap = [-n for n in nums]
       heapq.heapify(maxHeap)
       res = None
       while k > 0 :
            res = heapq.heappop(maxHeap)
            k -= 1
       return (-1)*res
