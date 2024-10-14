class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for num in nums:
            if num in numbers:
                return True
        numbers.add(num)

        return False

