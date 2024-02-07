class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        l = 0
        r = 1

        for r in range(len(nums)):
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]

            if nums[l]!= 0:
                l += 1

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<=r:
            sum1 = numbers[l] + numbers[r]
            if sum1 > target:
                r -= 1
            elif sum1 < target :
                l += 1
            else:
                return [l+1,r+1]

            
