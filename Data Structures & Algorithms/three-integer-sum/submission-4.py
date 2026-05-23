class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            target = -1 * nums[i]
            while j < k:
                if (nums[j] + nums[k] > target):
                    k -= 1
                elif (nums[j] + nums[k] < target):
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    l = nums[j]
                    j += 1
                    k -= 1
                    while j < k and nums[j] == l:
                        j += 1
        return res

            
