class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency={}
        for num in nums:
            if num in frequency:
                frequency[num]=frequency[num]+1
            else:
                frequency[num]=1
        for num in nums:
            if frequency[num] >= 2:
                return True
        return False