class Solution:
    def twoSum(self, nums: list[2,7,11,15], target: (9)):
        d = {}  # Dictionary to store num: index
        for i  in range(0,len(nums)):
            values=nums[i] #index value
            v = target - values
            if values not in d:
                d[v]=i
            else:
                current_index=i
                prev_index=d[values]
                return [prev_index,current_index]

        