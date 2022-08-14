Input, n = input().split()
import itertools
l =list(itertools.combinations_with_replacement(sorted(Input),int(n)))

print(*[''.join(i) for i in l], sep="\n")