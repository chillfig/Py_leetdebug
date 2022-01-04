class Solution:    
    nums = None
    val = None
    answer = None

    def __init__(self, nums, val) -> answer:
        self.nums = nums
        self.val = val
        self.answer = self.removeElement(self.nums, self.val)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # fill this in
    def removeElement(self, nums: list([int]), val: int) -> int:
        unique_index = 0
        for i in range(len(nums)):
            # if this a number we want
            if nums[i] != val:
                nums[unique_index] = nums[i]
                unique_index += 1
        return unique_index

example = Solution([0,1,1,1,2],1)
# expected output: 2 (nums:[0,2,_,_,_])
example1 = Solution([3,2,2,3],3)
# expected output: 2 (nums:[2,2,_,_])
example2 = Solution([0,1,2,2,3,0,4,2],2)
# expected output: 5 (nums:[0,1,3,0,4,_,_,_])
example3 = Solution([], 0)
# expected output: 0 (nums:[])