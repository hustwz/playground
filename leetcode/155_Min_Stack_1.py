class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_value = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.data) == 0:
            self.data.append(0)
            self.min_value = x
        else:
            tmp = x - self.min_value
            self.data.append(tmp)
            self.min_value = x if tmp < 0 else self.min_value

    def pop(self):
        """
        :rtype: void
        """
        if self.data[-1] < 0:
            self.min_value = self.min_value - self.data[-1]
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data[-1] < 0:
            return self.min_value
        else:
            return self.data[-1] + self.min_value

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
