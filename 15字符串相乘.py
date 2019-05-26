class Solution(object):
    def permute(self, nums) :
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = 0
        for i in enumerate(num1[::-1]):
            temp_num2 = 0
            for j in enumerate(num2[::-1]):
                temp_num2 += int(j[1])*pow(10, j[0])
            temp += int(i[1])*pow(10,i[0])*temp_num2
        return str(temp)

if __name__ == '__main__':
    s = Solution()
    print(s.multiply("12","12"))