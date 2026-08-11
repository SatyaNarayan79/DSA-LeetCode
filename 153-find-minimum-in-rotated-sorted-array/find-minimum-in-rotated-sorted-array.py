class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        target = float("inf")
        n=len(nums)
        n=len(nums)
        for i in range(0,n):
          if target > nums[i]:
            target=nums[i]
        return target 