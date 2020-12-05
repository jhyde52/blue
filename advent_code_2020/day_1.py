
# open file and use set to optimize
with open("input_1.txt") as _file:
    nums = [int(line) for line in _file]
    set_nums = set(nums)

# if the sum of two entries is 2020, multiply them and return the result
def part_one(nums, set_nums):
    for num in nums:
        if 2020 - num in set_nums:
            return num * (2020 - num)

# what is the product of the three entries that sum to 2020?
def part_two(nums, set_nums):
    for num in nums:
        for num2 in nums:
            if (2020 - num - num2) in set_nums:
                return num * (2020 - num - num2) * num2

print("Part 1", part_one(nums, set_nums))
print("Part 2", part_two(nums, set_nums))
