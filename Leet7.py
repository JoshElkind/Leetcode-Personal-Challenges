class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = []

        for i in range(len(nums)):
          if len(stack) != 0 and stack[0] == i-k:
            stack.pop(0)
          while len(stack) != 0 and nums[stack[len(stack)-1]] < nums[i]:
            stack.pop()
          
          stack.append(i)
          if i >= k-1:
            ans.append(nums[stack[0]])
        return ans