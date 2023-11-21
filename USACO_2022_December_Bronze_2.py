
inf = float('inf')

def fix(lineup,k,setup,ln):
    starts = []
    last_g = -inf
    last_h = -inf
    for i,itm in enumerate(lineup):
        if itm == 'G':
            if i-last_g > 2*k:
                starts.append([i,'G'])
                last_g = i
        else:
            if i-last_h > 2*k:
                starts.append([i, 'H'])
                last_h = i
    for i,char in starts:
        for pos in range(min(i+k,ln-1),-1,-1):
            if setup[pos] == '.':
                setup[pos] = char
                break
    return len(starts),''.join(setup)

for tc in range(int(input())):
    n,k = input().split()
    n,k = int(n),int(k)
    lineup = input()
    p,l = fix(list(lineup),k,['.']*n,n)
    print(p)
    print(l)
