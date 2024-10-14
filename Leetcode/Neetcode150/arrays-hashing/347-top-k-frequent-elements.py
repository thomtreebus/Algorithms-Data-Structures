class Solution:
    '''
    intuition: each element can occur between 1-n times (either all unique or n same elements)
    for each frequency 1-n, find the elements that occur that many times
    since the solution is guaranteed to be unique, we don't need
    to worry about ties (i.e. two elements occuring the same num. of times in top k)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        buckets = [[]] * (len(nums) + 1)
        for element in frequency.keys():
            freq = frequency[element]
            if buckets[freq]:
                buckets[freq].append(element)
            else:
                buckets[freq] = [element]
        
        res = []
        for i in range(len(nums), -1, -1):
            if buckets[i] and k > 0:
                for element in buckets[i]:
                    res.append(element)
                    k -= 1

        return res