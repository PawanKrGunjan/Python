def firstElementKTime(a, n, k):
    # code here
    dict = {}
    for i in range(n):
        if a[i] in dict.keys():
            dict[a[i]] += 1
        else:
            dict[a[i]] = 1

        if dict[a[i]] == k:
            return a[i]
    return -1

arr = [1, 7, 4, 3, 4, 8, 7]
n = 7
k =2
print(firstElementKTime(arr, n, k))
