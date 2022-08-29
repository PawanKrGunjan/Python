class Solution:
    def rearrange(self,arr, n):
        positive = []
        negative = []
        for num in arr:
            if num >= 0:
                positive.append(num)
            else :
                negative.append(num)

        P = len(positive)
        N = len(negative)
        if P > N:
            arr[:N+P] = [num[item] for item in range(len(negative)) for num in [positive, negative]]
            arr[N+P:] = positive[N:P]
        else:
            arr[:N+P] = [num[item] for item in range(len(positive)) for num in [positive, negative]]
            arr[N+P:] = negative[P:N]
        return arr



l1= [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
l2 = [1,-1, 3, -3, 4, -4, -5]
l3 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
ob = Solution()
ob.rearrange(l1, len(l1))
ob.rearrange(l2, len(l2))
ob.rearrange(l3, len(l3))

print(l1)
print(l2)
print(l3)
