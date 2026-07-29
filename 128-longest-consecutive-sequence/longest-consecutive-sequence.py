class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        set1=set(nums)
        largest=0
        for num in set1:
            if num-1 not in set1:
                x=num
                count=1
                while x + 1 in set1:
                    count += 1
                    x += 1
                largest=max(largest,count)
        return largest        