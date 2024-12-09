class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 1
        op = []
  
        pre = 1
        post = 1

        for num in nums:
            op.append(pre)
            pre *= num
        print(op)
        for i in range(len(nums) - 1, -1, -1):
            op[i] = op[i] * post
            post *= nums[i]
            print(post)
        

        return op
