import random
from typing import List


class Solution:

    def random_set(self):
        for x in range(0, self.numMax):
            self.nums.append(int(random.random() * self.randMax))
        idx1 = int(random.random() * (self.numMax - 1))
        idx2 = int(random.random() * (self.numMax - 1))
        self.target = self.nums[idx1] + self.nums[idx2]

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target[0]:
                    output.append(i)
                    output.append(j)
                    break
                if len(output) > 0:
                    break
        return output

    def __init__(self):
        self.nums = []
        self.target = 0
        self.numMax = 10
        self.randMax = 10000
        self.random_set()
        self.output = self.two_sum(self, self.nums, self.target)

    print(output)