def main(nums):
    nums.sort()
    n = len(nums)

    for i in range(1, n):
        if nums[i-1] == nums[i]:
            print(True)

    print(False)


main([1,2,3,1])