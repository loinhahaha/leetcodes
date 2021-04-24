# Find any reappear number in list.
# Input: [2, 3, 1, 0, 2, 5, 3]
# OutputA: 2
# OutputB: 3
# Tip: Use a dict as hash map

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1
    
