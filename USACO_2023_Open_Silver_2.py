'''
C,N = input().split()
C,N = int(C),int(N)
running = [0]*N
values = [input() for line in range(N)]
def solution2(strings):
    table = str.maketrans('GH', '01')
    numbers = [
        int(s.translate(table), 2)
        for s in strings
    ]
    L = len(strings[0])
    bits = [2**i for i in range(L)]
    dist = [None] * 2**L
    for x in numbers:
        dist[x] = 0
    horizon = numbers
    d = 1
    while horizon:
        horizon = [
            y
            for x in horizon
            for bit in bits
            for y in [x ^ bit]
            if dist[y] is None
            for dist[y] in [d]
        ]
        d += 1
    return [L - dist[~x] for x in numbers]
for final in solution2(values):
    print(final)
'''

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
