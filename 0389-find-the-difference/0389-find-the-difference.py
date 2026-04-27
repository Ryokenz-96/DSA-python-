class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        ctr1=Counter(t)
        ctr2=Counter(s)
        if ctr1!=ctr2:
            keys=list((ctr1-ctr2).keys())
            return keys[0]