class Solution(object):
    def reverseString(self, s):
        r=len(s)-1
        l=0
        while l<r:
	        s[l],s[r]=s[r],s[l]
	        l+=1
	        r-=1
        return s
        
        