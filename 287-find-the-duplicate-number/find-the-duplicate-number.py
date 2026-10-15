class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        fz_map = dict()
       # useing fz_map mapping 
        for i in range(0,n):
            if nums[i] in fz_map:
                return nums[i]

            else:
                fz_map[nums[i]] = 1
