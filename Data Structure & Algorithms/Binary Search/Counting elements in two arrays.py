
class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        D = {}
        s = list(set(arr1))
        arr2.sort()
        for i in s:
            left_index = 0
            right_index = n2-1
            while left_index <= right_index:
                mid = (left_index + right_index)//2
                if arr2[mid] > i:
                    right_index = mid - 1
                else:
                    left_index = mid + 1
            D[i]= right_index+1
        
        return [D[j] for j in arr1]

           
if __name__ == '__main__':
    '''
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
    '''
    arr1 = [1,2,3,4,7,9]
    arr2 = [0,1,2,1,1,4]
    res = Solution().countEleLessThanOrEqual(arr1,len(arr1),arr2,len(arr2))
    for i in range (len (res)):
        print (res[i], end = " ")
    print("\n************")