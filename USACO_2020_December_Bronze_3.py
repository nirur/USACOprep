ln = int(input())
cows = [input().split() for itm in range(ln)]
inf = float('infinity')
finals = [None]*ln
cows = [(dr,int(a),int(b)) for dr,a,b in cows]

queue = []

for ind1,i in enumerate(cows):
    if i[0] == 'E':
        continue
    for ind2,j in enumerate(cows):
        if j[0] == 'N':
            continue
        xdiff = i[1]-j[1]
        ydiff = j[2]-i[2]
        if xdiff<0 or ydiff<0:
            continue
        if xdiff>ydiff:
            queue.append((xdiff,ydiff,ind2,ind1))
        elif ydiff>xdiff:
            queue.append((ydiff,xdiff,ind1,ind2))

queue.sort()
for dist,stopdist,val,stop in queue:
    if not finals[stop] or finals[stop]>stopdist:
        if finals[val]:
            finals[val] = min(finals[val],dist)
        else:
            finals[val] = dist

for itm in finals:
    if itm:
        print(itm)
    else:
        print('Infinity')

