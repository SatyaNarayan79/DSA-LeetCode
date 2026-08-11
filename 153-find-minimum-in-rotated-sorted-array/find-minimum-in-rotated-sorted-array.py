class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        target = float("inf")
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            if nums[low]<=nums[high]:
                if target > nums[low]:
                    target=nums[low]
                low+=1
            else:
                if target > nums[high]: 
                    target=nums[high]
                high-=1
            
        return target