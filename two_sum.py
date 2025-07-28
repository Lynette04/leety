#This is the famous two sum solution where a person enters a target number which is supposed to be a sum of any two numbers in the given array and it returns the position of the two numbers which when added together give the target.
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # If no solution is found

nums=[2,3,4,5]
target=int(input("Give a number which is a sum of two numbers in the array:"))
result = two_sum(nums,target)

if result:
    print("Indices are: ",result)
else:
    print("Target not found")