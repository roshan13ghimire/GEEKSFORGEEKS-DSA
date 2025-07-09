class Solution:
    def findElements(self,arr):
        self.quicksort(arr,0,len(arr)-1)
        return arr[:len(arr)-2]
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low - 1
        for j in range(low,high):
            if arr[j] < pivot:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    def quicksort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr,low,high)
            self.quicksort(arr,low,pi-1)
            self.quicksort(arr,pi+1,high)
    
