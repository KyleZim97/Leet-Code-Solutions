def main(nums):
    numSet = set()

    for n in nums:
        if n in numSet:
            print(True)
        else:
            numSet.add(n)

    print("False")

main([1,2,3,1])