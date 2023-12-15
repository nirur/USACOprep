input()
s = input()
base = 0
l = len(s)
for x in range(l-1):
    if s[x]==s[x+1]!='F':
        base += 1
def lcount(st):
    for i,char in enumerate(st):
        if char != 'F':
            return i
    return i+1
ldel = lcount(s)
rdel = lcount(s[::-1])
if ldel==rdel==l:
    complete = l-1
    s = ''
else:
    complete = ldel+rdel
    if rdel:
        s = s[ldel:-rdel]
    else:
        s = s[ldel:]
parses = []
while s:
    ind = s.find('F')
    if ind==-1:
        break
    s = s[ind-1:]
    lft = lcount(s[1:])
    parses.append(s[:lft+2])
    s = s[lft+1:]
dbls = 0
for p in parses:
    l = len(p)
    if not l:
        continue
    if p[0]==p[-1]:
        if l%2:
            base += 0
        else:
            base += 1
        dbls += (l-1)//2
    else:
        if l%2:
            base += 1
        else:
            base += 0
        dbls += (l-2)//2
if complete:
    final = range(base,2*dbls+1+complete+base)
else:
    final = range(base,2*dbls+base+1,2)
final = list(final)
print(len(final))
for itm in final:
    print(itm)
