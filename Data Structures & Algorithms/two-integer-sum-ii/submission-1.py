class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers) -1):
            p = i + 1
            while target - numbers[i] > numbers[p] and p < len(numbers) - 1:
                p+=1

            if target - numbers[i] == numbers[p]:
                return [i+1,p+1]

