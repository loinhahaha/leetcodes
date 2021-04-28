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
# TC: O(N)
# SC: O(N)

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
# TC: O(N)
# SC: O(1)

'''
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-yua/
'''
