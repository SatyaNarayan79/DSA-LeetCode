class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum=0
        n=len(nums)
        totalsum=(n*(n+1))//2
        for i in nums:
            sum=sum+i
        miss=totalsum-sum
        return miss    
