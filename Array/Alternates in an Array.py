class Solution:
    def getAlternates(self, arr):
        l = []
        for i in range(0,len(arr),2):
            l.append(arr[i])
        return l
