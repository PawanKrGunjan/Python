
# Enter your code here. Read input from STDIN. Print output to STDOUT
num = input()
import itertools
for key, group in itertools.groupby(num):
    print(f'({len(list(group))}, {key})',end=" ")
    