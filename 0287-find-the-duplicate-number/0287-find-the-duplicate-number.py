class Solution(object):
    def findDuplicate(self, nums):
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow2==slow:
                return slow