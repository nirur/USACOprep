with open('lemonade.in','r') as f:
    read_raw = f.read()
    n,waits,useless = read_raw.split('\n')
n = int(n)
waits = sorted([int(i) for i in waits.split()])
left = 0
blocked = 0
while left + blocked < n:
    blocked += 1
    while waits[left] < blocked:
        left += 1
with open('lemonade.out','w') as f:
    f.write(str(blocked)+'\n')
