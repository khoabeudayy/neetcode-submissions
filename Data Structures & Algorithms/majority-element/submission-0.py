class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            if n % 2 != 0:
                if nums.count(nums[0]) > n // 2:
                    return nums[0]
                nums = nums[1:]

            survivor = []
            for i in range(0, len(nums), 2):
                if nums[i] == nums[i+1]:
                    survivor.append(nums[i])

            nums = survivor

        return nums[0]