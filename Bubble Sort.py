class BubbleSort:
    def __init__(self,nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums)-1-i):
                if self.nums[j] > self.nums[j+1]:
                    self.swap(j,j+1)

    def swap(self,i,j):
        self.nums[i],self.nums[j] = self.nums[j],self.nums[i]


# algo = BubbleSort([10,5,3,8,2,12,55,2])
# algo.sort()
# print(algo.nums)




