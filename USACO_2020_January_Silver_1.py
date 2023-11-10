with open('berries.in','r') as f:
    BASKETS,TREES,discard = f.read().split('\n')
    K = int(BASKETS.split()[1])//2
    TREES = sorted([int(k) for k in TREES.split()])

def find(boundary):
    lst = chop(boundary,TREES)
    return sum(lst[-K*2:-K])

def chop(boundary,lst):
    first = []
    second = []
    for l in lst:
        second += [boundary]*(l//boundary)
        first.append(l%boundary)
    return sorted(first)+second
with open('berries.out','w') as f:
    f.write(str(max([find(k) for k in range(TREES[0],TREES[-1]+1)]))+'\n')
