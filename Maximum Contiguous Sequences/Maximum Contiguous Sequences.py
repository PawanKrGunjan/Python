'''
Maximum Contiguous Sequences
**Given an array of N integers, determine all contiguous subsequences of positive numbers. Then write a function to find the sum of elements each sub-sequence and output the maximum sum value.**
Input Specifiction:
**input1**: An integer N denoting length of array
**input2**: An integer array of length N(-10000<=A[i]<=10000)
Output Specification
**Return the maximum sum of contiguous sub-sequence of numbers**
'''


class UserMainCode(object):
    def __init__(self, n, a):
        self.i1 = n
        self.i2 = a

    @classmethod
    def FindContiguousSeq(cls, n, a):
        sum = [a[0]]
        for i in range(1, n):
            if sum[i-1]+a[i] > a[i]:
                sum.append(sum[i-1]+a[i])
            else:
                sum.append(a[i])
        return max(sum)


input1 = int(input())
input2 = [int(i) for i in input().strip('{}').split(',')]

print(UserMainCode.FindContiguousSeq(input1, input2))
