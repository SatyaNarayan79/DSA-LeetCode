class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        po=-1
        low=0
        high=n-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid] == target:
                po=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1    
            else:
                low=mid+1  
        return po          
