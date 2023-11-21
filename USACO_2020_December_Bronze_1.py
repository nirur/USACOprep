nums = [int(k) for k in input().split()]
nums.sort()
print(nums[0],nums[1],nums[-1]-nums[0]-nums[1])
