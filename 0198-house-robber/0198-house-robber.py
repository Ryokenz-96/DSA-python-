class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1,prev2=0,0
        for i in nums:
            rob=prev2+i
            skip=prev1
            best=max(rob,skip)
            prev2=prev1
            prev1=best
        return best