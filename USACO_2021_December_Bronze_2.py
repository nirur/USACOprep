l = int(input())
mx = 0
changes = [int(end)-int(start) for start,end in zip(input().split(),input().split())]
prv = 0
cnt = 0
for c in changes:
    if prv*c < 0:
        cnt += abs(c)
    elif abs(c) > abs(prv):
        cnt += abs(c-prv)
    prv = c
print(cnt)
