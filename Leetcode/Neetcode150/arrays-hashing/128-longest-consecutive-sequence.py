class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numbers:
                current = num + 1
                while current in numbers:
                    current += 1
                longest = max(longest, current - num)

        return longest