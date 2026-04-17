class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            dict[i]=0
        for i in nums:
            dict[i]=dict[i]+1
        for i in dict.values():
            if i>1:
                return True
        return False