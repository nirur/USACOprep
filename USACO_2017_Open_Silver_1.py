with open('pairup.in','r') as f:
    times = []
    for a in f.read().split('\n')[1:-1]:
        p,q = a.split()
        times += [[int(p),int(q)]]
    times.sort(key=lambda x: x[1])
m=0
print(times)
while times:
    if len(times) == 1:
        m = max(m,2*times[0][1])
        break
    mn = min(times[0][0],times[-1][0])
    times[0][0] -= mn
    times [-1][0] -= mn
    if not times[0][0]:
        times.pop(0)
    if times and not times[-1][0]:
        times.pop(-1)
    m = max(m, times[0][1]+times[-1][1])
with open('pairup.out','w') as f:
    f.write(str(m)+'\n')
