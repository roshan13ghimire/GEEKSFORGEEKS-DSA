class Solution:
    def reverseArray(self, arr):
        l = 0
        r = len(arr)-1
        while l<r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l+=1
            r-=1
        return arr
            
        
        
