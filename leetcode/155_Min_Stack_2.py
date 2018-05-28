class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_value = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if len(self.min_value) == 0 or x <= self.min_value[-1]:
            self.min_value.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.data[-1] == self.min_value[-1]:
            self.min_value.pop()
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
