class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1 
                # we don't increment i here because it needs to processed after the swap
                # with right position, as we are not aware if the element swapped is 0, 1, or 2.
            else: 
                i += 1 # 1 will remain in the middle of all 0s on the left and 2s on the right