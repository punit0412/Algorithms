def mergesort(nums):

    if len(nums) == 1: return

    # DIVIDE PHASE
    middle_index = len(nums)//2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]
    mergesort(left_half)
    mergesort(right_half)

    # CONQUER Phase
    i,j,k = 0,0,0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j +=1
        k += 1

    while i <len(left_half):
        nums[k] = left_half[i]
        i +=1
        k+=1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1

x = [25,1,8,3,-1,56,75,12,32]
mergesort(x)
print(x)
