class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for non_zero in nums:
            if non_zero!=0:
                nums[count]=non_zero
                count+=1
        for ze_ro in range(count,len(nums)):
            nums[ze_ro]=0

        