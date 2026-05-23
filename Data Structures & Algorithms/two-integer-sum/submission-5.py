class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}
        result = []
        for i, num in enumerate(nums):
            numIndices[num] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numIndices and numIndices[diff] != i:
                return [i, numIndices[diff]]
        return []


        