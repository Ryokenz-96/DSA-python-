class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num,occur=0,0
        for i in range(len(nums)):
            if occur==0:
                num=nums[i]
                occur=1
            elif num==nums[i]:
                occur+=1
            else:
                occur-=1
        return num