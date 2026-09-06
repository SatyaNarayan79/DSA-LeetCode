class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        seen =set()
        for i in range(0,n):
            seen.add(nums[i])
        for i in range(1,n+1):    
             if i not in seen:
                result.append(i)
        return result    