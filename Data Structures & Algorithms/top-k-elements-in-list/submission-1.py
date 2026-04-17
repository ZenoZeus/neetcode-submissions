class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        lst=[]
        for i in nums:
            dict[i]=0
        for i in nums:
            dict[i]=dict[i]+1
        dictList =sorted(dict.items(),key =lambda x:x[1],reverse=True)
        for i in range(k):
            lst.append(dictList[i][0])
        return lst