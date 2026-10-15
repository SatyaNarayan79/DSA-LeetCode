class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        water = 0
        temp = 0
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         water = (j-i) * min(height[i],height[j])
        #         if water > temp:
        #             temp = water
        # return temp   
        i = 0
        j = n-1
        while i < j:
            water = (j-i) * min(height[i],height[j])
            if water > temp:
                temp = water
            if height[i] <= height[j]:
                i += 1
            else:    
                j -= 1
        return temp    
