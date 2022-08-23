from collections import deque

class Queue:
    def __init__(self):
        self.row = deque()

    def enqueue(self, val):
        self.row.appendleft(val)

    def dequeue(self):
        return self.row.pop()

    def is_empty(self):
        return len(self.row) == 0

    def size(self):
        return len(self.row)

pd = Queue()


pd.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
    })
pd.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
    })
pd.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
    })

print(pd.size())
print(pd.row)
pd.dequeue()
print(pd.is_empty())
pd.dequeue()
print(pd.size())
pd.dequeue()
print(pd.is_empty())