class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0 #first index
        high = len(s)-1 #last index
        while low < high:
           # In place swapping
            s[low],s[high] = s[high],s[low]
            low+=1
            high-=1

           