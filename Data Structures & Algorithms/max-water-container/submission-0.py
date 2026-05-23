class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                res = max(res, (j-i)*min(heights[j], heights[i]))
        return res
        