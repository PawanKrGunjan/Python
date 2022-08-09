'''
**input1:** Length of the array

**input2:** An array of positive integers

**Output Specification:**
Return the second largest number or -1 accordingly.
'''
'''
input1 = 3
input = 2,3,5
'''


class UserMainCode(object):
    def __init__(self, n, m):
        self.i1 = n
        self.i2 = m

    @classmethod
    def secondLargest(self, n, m):
        m.sort()
        for i in range(1, n):
            if m[n - i] != m[n - i - 1]:
                r = m[n - i - 1]
                break
            elif n - i == 1:
                r = -1
                break
            else:
                pass
        return r


input1 = int(input())
input2 = [int(i) for i in input().strip('{}').split(',')]
print(UserMainCode.secondLargest(input1, input2))
