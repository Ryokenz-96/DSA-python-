class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen={}
    for i,n in enumerate(nums):
        another=target-n
        if another in seen:
            return [seen[another],i]
        else:
            seen[n]=i
