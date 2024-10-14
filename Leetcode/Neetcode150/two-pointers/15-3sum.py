class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for left in range(len(nums) - 1):
            if left == 0 or nums[left] != nums[left-1]:
                mid = left + 1
                right = len(nums) - 1
                
                # find all triplets starting at left
                while mid < right:
                    s = nums[mid] + nums[right] + nums[left]
                    
                    if s > 0:
                        right -= 1
                    elif s < 0:
                        mid += 1
                    else:
                        res.append([nums[left], nums[right], nums[mid]])
                        # move pointers to prevent duplicates
                        while mid < right and nums[mid] == nums[mid + 1]:
                            mid += 1
                        while mid < right and nums[right] == nums[right - 1]:
                            right -= 1
                        mid += 1
                        right -= 1
        
        return res