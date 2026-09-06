class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        smaller = float('inf')
        temp = 0
        result = []
        for i in range(0,n):
            count = 0
            for j in range(0,n):
                if nums[i] > nums[j]:
                    count+=1
                
            temp = count 
            result.append(temp) 
        return result    

