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
            # if the current num is a complement of a past iteration, return
            if num in hashmap:
                return [hashmap[num], index]
            # otherwise, store the index of this num with the current complement as key
            hashmap[complement] = index
        return []


example1 = Solution([1,2,4], 3)
