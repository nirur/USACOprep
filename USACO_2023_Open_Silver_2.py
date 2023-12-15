c,n = input().split()
c = int(c)
n = int(n)
dists = [None]*2**c
changes = [2**k for k in range(c)]
hit = set()
beginnings = []
starts = []
for x in range(n):
    i = eval('0b'+input().replace('G','0').replace('H','1'))
    starts.append(i)
    dists[i-1] = 0
    hit.add(i)
beginnings = starts
dist = 1
while starts:
    tmp = []
    tmpst = set()
    for itm in starts:
        for ch in changes:
            changed = itm+ ch-(itm%(ch*2))*2+(itm%ch)*2
            if changed not in hit:
                dists[changed-1] = dist
                tmp.append(changed)
                hit.add(changed)
    starts = tmp
    dist += 1
for x in range(n):
    print(c-dists[2**c-beginnings[x]-2])
