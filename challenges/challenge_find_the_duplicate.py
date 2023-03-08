def find_duplicate(nums):
    if len(nums) < 2:
        return False
    
    sorted_nums = sorted(nums)
    number = 0
    
    for n in range(number, len(nums) - 1):
        if sorted_nums[n] == sorted_nums[n + 1]:
            number = sorted_nums[n]
    if not number or number < 1:
        return False

    return number
