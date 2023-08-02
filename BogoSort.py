import random
class BogoSort:
    def __init__(self,nums):
        self.nums = nums

    def sort(self):
        while not self.is_sorted():
            print('Shuffle...')
            self.shuffle()

    # Fisher - yates approach
    def shuffle(self):
        for i in range(len(self.nums)-2,-1,-1):
            j = random.randint(0,i+1)
            self.nums[i],self.nums[j] = self.nums[j],self.nums[i]

    def is_sorted(self):
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False
        return True

if __name__ == '__main__':
    algo = BogoSort([45,-5,3,8,5,68,2,8157,12])
    algo.sort()
    print(algo.nums)