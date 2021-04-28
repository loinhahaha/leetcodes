# Input an integer array, output array all odd numbers are in the first half of the array, and all even numbers are in the second half of the array
# Fast low pointers
# Double pointers

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i, j = 0, 0
        while j < N:
            if nums[j]%2 ==1:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            
            j+=1
        return nums
      
        N = len(nums)
        i, j = 0, N-1
        while i < j:
            if nums[i] % 2 ==1: 
                i+=1
                continue 
            if nums[j] % 2 ==0:
                j-=1
                continue
            nums[i],nums[j] = nums[j],nums[i]
        return nums
# TC: O(N)
# SC: O(1)      
