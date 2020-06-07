# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

class Solution:
    def reverse(x: int) -> int:
        s = str(x)[::-1].rstrip('-')  # [::1]的作用是反转字符串，rstrip('-')是去除负号“-”
        if int(s) < 2 ** 31:
            if x >= 0:
                return int(s)
            else:
                return 0 - int(s)
        return 0


x = '-123'
ob = Solution.reverse(x)
print(ob)
