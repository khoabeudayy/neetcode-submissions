class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for a,b in enumerate(nums):
            diff = target - b
            if diff in result:
                return [result[diff],a]
            result[b] = a 



        