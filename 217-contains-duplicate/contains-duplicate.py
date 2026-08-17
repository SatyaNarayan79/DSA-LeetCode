class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n=len(nums)
        my_set=set()
        for i in range(0,n):
            if nums[i] in my_set:
                return True
            
            my_set.add(nums[i])    
        return False    