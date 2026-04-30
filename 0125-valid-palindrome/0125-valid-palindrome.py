class Solution:
    def isPalindrome(self, s: str) -> bool:
        another=''
        for i in s.lower():
            if i.isalnum():
                another+=i
        return another[::-1]==another