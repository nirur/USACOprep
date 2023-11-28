n,t = map(int,input().split())
day = 1
food = 0
total = 0
data = [map(int,input().split()) for np in range(n)]+[[t+1,0]]
for di,bi in data:
    diff = di-day
    total += min(food,diff)
    food = max(food-diff,0)+bi
    day = di
print(total)
