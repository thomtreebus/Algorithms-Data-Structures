class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            number = nums[i]
            if target - number in diffs:
                return [i, diffs[target - number]]
            diffs[number] = i