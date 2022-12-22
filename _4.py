#задание1

print(' '.join(input().split()[::2]))

#задание2

s = [int(i) for i in input().split()]
l = list()
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        l.append(s[i])
print(" ".join(str(i) for i in l))

#задание3

q = [int(i) for i in input().split()]
maxnum = max(q)
minnum = min(q)
for i in range(len(q)):
    if q[i] == maxnum:
        q[i] = minnum
    elif q[i] == minnum:
        q[i] = maxnum
print(q)

#задание4

def key(c, k):
    print(c.get(k))
    
#задание5
from figures import t_area
t_area()
