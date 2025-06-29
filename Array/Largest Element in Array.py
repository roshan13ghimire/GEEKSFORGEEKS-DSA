class Solution:
    def largest(self, arr):
        max = 0
        for i in range(len(arr)):
            if max < arr[i]:
                max = arr[i]
        return max
        
