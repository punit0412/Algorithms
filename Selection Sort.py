def selectionSort(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i,len(nums)):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            nums[index],nums[i] = nums[i],nums[index]
    return nums
nums = [1,8,5,6,7]
print(selectionSort(nums))


def insertionSort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j = j-1
    return nums

n = [10,5,3,8,2,12,55,2]
print(insertionSort(n))