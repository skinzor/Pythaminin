# floyd's tortoise and hare

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    pattern1 = nums[0]
    pattern2 = tortoise
    while pattern1 != pattern2:
        pattern1 = nums[pattern1]
        pattern2 = nums[pattern2]

    return pattern1


numbers = [4, 2, 5, 6, 7, 1, 4, 8, 9, 3]
duplicate_nums = findDuplicate(numbers)
print(duplicate_nums)
