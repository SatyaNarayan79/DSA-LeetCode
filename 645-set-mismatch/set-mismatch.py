class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        dupli=0
        
        for i in range(0,len(nums)):
            if nums[i] in seen:
                dupli = nums[i]
            else:
                seen.add(nums[i])    
        for i in range(1,len(nums)+1):    
            if i not in nums:
                return [dupli,i]        
