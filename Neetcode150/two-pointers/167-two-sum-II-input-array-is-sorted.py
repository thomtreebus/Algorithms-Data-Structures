class Solution:
    '''
    intuition: we can use the fact that the input array is sorted to our advantage. 
    By using two pointers at the ends of the array, we can simply check if the sum of the
    numbers at those indices is equal to the target. If it's larger than the target,
    then we know that we need to use a smaller value so we simply decrement the right pointer,
    the same is true for when the sum is smaller than the target.
    time: O(n)
    space: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            value = numbers[left] + numbers[right]
            if value == target:
                return [left + 1, right + 1]
            elif value < target:
                left += 1
            else:
                right -= 1