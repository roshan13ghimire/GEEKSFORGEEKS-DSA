class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(1,len(arr)-1):
            if arr[i-1] > arr[i]:
                return False
        return True
