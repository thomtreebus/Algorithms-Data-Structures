class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 1):
            if i == 0 or nums[i] != nums[i-1]:
                l = i + 1
                r = len(nums) - 1
                
                # find all triplets starting at i
                while l < r:
                    s = nums[l] + nums[r] + nums[i]
                    
                    if s > 0:
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:
                        res.append([nums[l], nums[r], nums[i]])
                        # move pointers to prevent duplicates
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        
        return res