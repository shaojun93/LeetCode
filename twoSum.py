# 1. 两数之和
#
# 题目描述：
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        a =set()
        lens = len(nums)
        for i in range(lens):
            if target - nums[i] in a:#判断（目标值-新遍历的元素）是否存在集合内元素与之相同
                return [i,nums.index(target-nums[i])]#返回新遍历的元素索引，index获得另外一个元素索引
            a.add(nums[i])#将遍历的列表元素存入集合

nums = [2,7,11,15]
target = 212
ob = Solution().twoSum(nums,target)
print(ob)