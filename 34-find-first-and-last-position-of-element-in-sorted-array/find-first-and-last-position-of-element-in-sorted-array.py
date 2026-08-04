class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstocc(nums,target):
            n=len(nums)
            lb=-1
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb
        def lastocc(nums,target):
            n=len(nums)
            ub=-1
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            return ub  
                         
        lb =firstocc(nums, target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub =lastocc(nums, target)
        if nums[len(nums) - 1] == target:
            return [lb, len(nums) - 1]

        return [lb, ub - 1]

        