class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lb(nums,target,n):
            lb = -1
            low = 0
            high = n-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] >= target:
                    lb = mid
                    high = mid-1
                else:
                    low = mid+1
            return lb      
        def ub(nums,target,n):
            ub = n
            low = 0
            high = n-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid]>target:
                    ub=mid
                    high = mid-1
                else:
                    low = mid +1  
            return ub   
            

    
        n=len(nums) 
        first = lb(nums,target,n)
        second = ub(nums,target,n)
        if first == -1 or nums[first] != target:
            return [-1, -1]
        return [first,second-1]                  
                   

