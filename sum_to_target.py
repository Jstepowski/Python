from operator import indexOf


def get_index(nums, target):
    first = nums[0]
    for i in range (0, len(nums)-1):
        for j in range (1, len(nums)):
            if nums[i] + nums[j] == target:
                print (nums[i], nums[j])
                return nums.index(nums[i]), nums.index(nums[j])


nums = [1, 3, 7]
target = 10
results = get_index(nums, target)
print (results)
