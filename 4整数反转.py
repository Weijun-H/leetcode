class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit_max = pow(2,31)-1
        limit_min = -pow(2,31)
        str_x = str(x)
        if str_x[0] == '-':
            answer =  int(str_x[0] + str_x[:0:-1])
        else:
            answer =  int(str_x[::-1])
        if answer>= limit_min and answer <= limit_max:
            return answer
        else :
            return 0