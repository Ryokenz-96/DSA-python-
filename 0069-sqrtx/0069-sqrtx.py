class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                result=mid
                left=mid+1
            if mid*mid>x:
                right=mid-1
        return result