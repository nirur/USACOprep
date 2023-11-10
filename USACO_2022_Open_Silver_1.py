n = int(input())
vls = [0]*n
tally = 0
bnxt = [0]*2*n
for x in range(n):
    i = input().split()
    p = bnxt[x+n] = int(i[0])-1
    q = vls[x] = int(i[1])
    bnxt[p] += 1
    tally += q
del p
del q
def gen():
    for itm in queue:
        bnxt[bnxt[itm-1+n]] -= 1
        k = bnxt[itm-1+n]
        bnxt[itm-1+n] = 0
        yield k
queue = [
    k+1
    for k in range(n)
    if not bnxt[k]
]
while queue:
    queue = [
        k+1
        for k in gen()
        if not bnxt[k] and bnxt[k+n]
    ]
for x in range(n):
    if bnxt[x]:
        mn = vls[x]
        while bnxt[x]:
            mn = min(mn, vls[x])
            bnxt[x] = 0
            x = bnxt[x+n]
        tally -= mn
print(tally)
