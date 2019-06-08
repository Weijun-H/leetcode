class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minstack) == 0:
            self.minstack.append(x)
        elif self.minstack[-1] < x:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return False
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        print('stack:{}'.format(self.stack))
        print('minstack:{}'.format(self.minstack))
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()