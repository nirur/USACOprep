input()
nms = [int(a) for a in input().split()]
nms.sort(key=lambda x:-x)
mx = 0
sm = 0
tuition = 0
for i,itm in enumerate(nms):
    k = (i+1)*itm
    if k>=mx:
        mx=k
        tuition = itm
print(mx,tuition)
