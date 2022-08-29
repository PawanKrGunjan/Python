import bisect as bt

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        arr2.sort()
        res = []
        for e in arr1:
            res.append(bt.bisect(arr2,e))
            
        return res

if __name__ == '__main__':
    arr1 = [1,2,3,4,7,9]
    arr2 = [0,1,2,1,1,4]
    res = Solution().countEleLessThanOrEqual(arr1,len(arr1),arr2,len(arr2))
    for i in range (len (res)):
        print (res[i], end = " ")
    