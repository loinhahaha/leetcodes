# Rotate list: Move the first elements of an ascending array to the end of the array.
# [1,2,3,4,5] -> [3,4,5,1,2] 
# Tip: Use ichotomy algorithm.

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers)-1

        while i<j:
            mid = (i + j) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            elif numbers[mid] < numbers[j]:
                j = mid
            else: j -= 1
        return numbers[i]

    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]
