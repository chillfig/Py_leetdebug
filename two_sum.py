class Solution:    
    nums = None
    target = None
    answer = None

    def __init__(self, nums, target) -> answer:
        self.nums = nums
        self.target = target
        self.answer = self.twoSum(self.nums, self.target)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # fill this in
    def twoSum(self, nums, target) -> list:
        hashmap = {}
        # iterate through each number in list O(n)
        for index, num in enumerate(nums):
            # identify the complement needed to satisfy target
            complement = target - num
            # if we've seen the complement with a past iteration, return
            if complement in hashmap:
                return [index, hashmap[complement]]
            # otherwise, store the index of this num with the current complement as key
        return []


example1 = Solution([3,2,4], 6)
