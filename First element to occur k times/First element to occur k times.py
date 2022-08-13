print('''First element to occur k times
Given an array of N integers. 
Find the first element that occurs at least K number of times.''')
class Solution:
    def firstElementKTime(self,  a, n, k):
        x = [[1 for i in range(n)] for i in range(2)]
        for i in range(n):
            x[0][i]=a[i]
            for j in range(i):
                if a[i] == a[j]:
                    x[1][i] += 1
        try:
            return x[0][x[1].index(k)]
        except:
            return -1

def main():
    print('Enter the array value (1 7 4 3 4 8 7)')
    a = [int(x) for x in input().strip().split()]
    n = len(a)
    print('Enter the number of repeatation (2)')
    k = int(input())
    ob = Solution()
    print(ob.firstElementKTime(a, n, k))


if __name__ == "__main__":
    main()

