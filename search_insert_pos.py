class Solution:    
    nums = None
    target = None
    answer = None

    def __init__(self, nums, target) -> answer:
        self.nums = nums
        self.target = target
        self.answer = self.searchInsert(nums, target)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # 35. Search Insert Position
    def searchInsert(self, nums: list([int]), target: int) -> int:
        left = 0                    # LHS index of nums array
        right = len(nums) - 1       # RHS index of nums array
        
        while left < right:
            # assign the mid index
            mid = (left + right) // 2
            
            # case that we deal with RHS of nums from mid
            if target > nums[mid]:
                left = mid + 1
            # case that we deal with LHS of nums with mid inclusive
            # target is <= nums[mid]
            else: 
                right = mid
        return left

example1 = Solution([1,3,5,6],5)
# output: 2
example2 = Solution([1,3,5,6],2)
# output: 1
example3 = Solution([1,3,5,6],7)
# output: 4


def searchInsert(self, nums, target):
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)/2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

# def searchInsert(self, nums, target): # works even if there are duplicates. 
#     l , r = 0, len(nums)-1
#     while l <= r:
#         mid=(l+r)/2
#         if nums[mid] < target:
#             l = mid+1
#         else:
#             if nums[mid]== target and nums[mid-1]!=target:
#                 return mid
#             else:
#                 r = mid-1
#     return l