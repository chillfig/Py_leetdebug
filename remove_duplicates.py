class Solution:    
    nums = []
    answer = None

    def __init__(self, nums) -> answer:
        self.nums = nums
        self.answer = self.removeDuplicates(self.nums)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # fill this in
    def removeDuplicates(self, nums: list([int])) -> int:
        # case that duplicates can't exist so just return
        if len(nums) <= 1: return len(nums)
        
        unique_index = 0
        # start loop at second number in nums, we know the first index (0) must be unique
        for i in range(1, len(nums)):
            # case that we see a new, unique number in the list
            if nums[i] != nums[unique_index]:
                # starting with the second number in nums, replace with unique numbers
                nums[unique_index + 1] = nums[i]
                # keep track of times we've seen an unique number
                unique_index += 1
        # number of unique numbers in nums equals our index plus 1 for the 0th index
        return unique_index + 1

example1 = Solution([0,0,1,1,1,2,2,3,3,4])
# output: 5, nums = [0,1,2,3,4,_,_,_,_,_])
example2 = Solution([1,1,1,1])
# output: 1, nums = []