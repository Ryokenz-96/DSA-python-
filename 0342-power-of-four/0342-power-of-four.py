class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while True:
            if n%4==0 or n==1:
                if n==1:
                    return True
                else:
                    n=n//4
            else:
                return False