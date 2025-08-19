def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # variables
    found = False
    i = 0
    sol = []

    # solution
    while i < len(nums) and found == False:
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                found = True
                sol.append(i)
                sol.append(j)
            j += 1
        if found == False:
            i += 1
    
    return sol



def main():
    sol = []
    sol = twoSum([3,3], 6)

    for num in sol:
        print(num)

main()