class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele=[]
        for i in nums:
            if i not in ele:
                ele.append(i)
            elif i in ele:
                ele.remove(i)
        return ele[0]