class QuickSort:
    def __init__(self,nums):
        self.nums = nums

    def sort(self):
        self.quicksort(0,len(self.nums)-1)

    def quicksort(self,low,high):
        if low >= high:
            return
        pivot_index = self.partition(low,high)
        self.quicksort(low,pivot_index-1)
        self.quicksort(pivot_index+1,high)


    def partition(self,low,high):
        pivot_index = (low+high)//2

        self.nums[pivot_index],self.nums[high] = self.nums[high],self.nums[pivot_index]
        for i in range(low,high):
            if self.nums[i] <= self.nums[high]:
                self.nums[i],self.nums[low] = self.nums[low],self.nums[i]
                low += 1
        self.nums[low], self.nums[high] = self.nums[high], self.nums[low]

        return low

algo = QuickSort([25,1,8,3,-1,56,75,12,32])
algo.sort()
print(algo.nums)




