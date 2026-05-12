class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        ansLength = numsLength * 2
        ans = [0] * ansLength

        for i in range(0, numsLength):
            ans[i] = nums[i]
        for i in range(numsLength, ansLength):
            ans[i] = nums[i - numsLength]
        
        return ans
