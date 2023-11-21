input()
nums = [int(k) for k in input().split()]
prfx = [0]
sm = 0
for n in nums:
    sm += n
    prfx.append(sm)
l = len(nums)
final = 0
for start in range(l):
    for end in range(start,l):
        target = (prfx[end+1]-prfx[start])/(end-start+1)
        if int(target)!=target:
            continue
        for itm in nums[start:end+1]:
            if itm==target:
                final += 1
                break
print(final)
