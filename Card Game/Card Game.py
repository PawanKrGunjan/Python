'''
### The Card Game
One day, Fred and his N friends were playing a card game in which each player throws a card with a number written on it. The cards are such that a number X is written on front of the card, and the negative of that number is written on the back side of the card. This game has the following rules:-

Each of N players is asked to throw a card. After all the N cards are thrown,  Fred has to flip one or more cards in consecutive order, only once. 
Your task is to help Fred flip the cards in such a way that the sum of the numbers, on front face of the cards, is the maximum.

### Input Specifications
**input1:** An integer N denoting the number of cards(1<=N<=500)
**input2:** An integer array containing N integers, where the ith integer denotes the value on the front of the card(-1000<=input2[i]<=1000)
### Output Specifications
Return the maximum sum of the numbers, on the front of the cards
'''


class UserMainCode(object):

    def __init__(self, n, m):
        self.i1 = n
        self.i2 = m

    @classmethod
    def Cards(cls, n, m):
        s = []
        for i in range(n):
            o = []
            for j in range(n):
                if i > j:
                    o.append((m[j]))
                else:
                    o.append(-(m[j]))
            # print(o)
            s.append(sum(o))
        return max(s)


input1 = int(input())
input2 = [int(i) for i in input().strip('{}').split(',')]
print(UserMainCode.Cards(input1, input2))
