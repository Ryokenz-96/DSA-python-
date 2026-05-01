class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit=0
        num=x
        if num<0:
            return False
        while num!=0:
            rem=num%10
            digit=digit*10+rem
            num=num//10
        return digit==x