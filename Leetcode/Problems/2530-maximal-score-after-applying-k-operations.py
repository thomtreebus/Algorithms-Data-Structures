import heapq

class Solution:
    '''
    Building a heap takes O(n) time, insert (O(log n)), find-min (O(1)). Using the heap, we simply
    find the smallest element, add it to our sum, and then perform the ceil(current/3) operation. 
    Repeat k times and we have the solution in linear time. We invert each number in nums before
    starting since heapq.heapify uses a min heap, and I'm too lazy to use the weird max heap operations. 
    Time: O(n)
    Space: O(n)
    '''
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)
        score = 0 

        for i in range(k):
            current = heapq.heappop(nums)
            score += current

            heapq.heappush(nums, floor(current / 3))


        return score * -1