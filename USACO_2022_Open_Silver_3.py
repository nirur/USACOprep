prfx = [(0,0,0)]
c,o,w = 0,0,0
for char in input():
    if char == 'C':
        c ^= 1
    elif char == 'O':
        o ^= 1
    elif char == 'W':
        w ^= 1
    prfx.append((c,o,w))
out = ''
for i in range(int(input())):
    query = input().split()
    l,r = int(query[0]),int(query[1])
    left,right = prfx[l-1],prfx[r]
    final = [left[x]^right[x] for x in range(3)]
    k = final[1]+final[2]-final[0]
    if k==-1 or k==2:
        out += 'Y'
    else:
        out += 'N'
print(out)
